import hashlib
import os
import json
import sys

from textwrap import wrap
from lib.mixer import VideoMixer

################################# INPUTS

textsdir = "./textsdir/"

##################################



def getmd5(path) :
	try:
		with open(path, "rb") as f:
			bytes = f.read()
			return hashlib.md5(bytes).hexdigest();
	except: 
		pass
	
def files(path, exts) :
	result = []
	for file in os.listdir(path):
		newpath = path + "/" + file
		try:
			if not os.path.isfile(newpath):	
				result.extend(files(newpath, exts))
		except:
			pass
		for ext in exts:
			try:
				if os.path.isfile(newpath) and newpath.endswith(ext):
					result.append(newpath)
			except:
				pass
	return result
	


def getTextBytesFromTextDir(folder):
	string_from_files = ""	
	filestxt = files(folder, [".txt", ".TXT", '.html'])
	
	for file in filestxt:
		try:
			with open(file, 'r') as f:
				string_from_files += f.read()
		except:
			pass
				
	return string_from_files   

salt_bytes1 = getTextBytesFromTextDir(textsdir)

settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

settings["salts"] = salt_bytes1

if len(sys.argv) > 1 and "init" in sys.argv[1].split(","):
	settings["flags"] = ["init"]

print(settings)
vm = VideoMixer(settings)


while True:
	x = vm.run()
	if not x:
		break
#vm.run("i")
