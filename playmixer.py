import hashlib
import os
import json
import sys

from textwrap import wrap
from lib.mixer import VideoMixer


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
	
def getmd5(path) :
	try:
		with open(path, "rb") as f:
			bytes = f.read()
			return hashlib.md5(bytes).hexdigest();
	except: 
		pass
		
def getBytesFromImages(folder):	
	images = files(folder, [".jpg"])
	string_bytes = ""
	
	for i in images:
		sums = getmd5(i)
		wrapped = wrap(sums, 5)	
		string_bytes += " "+(" ".join(wrapped))
	
	return string_bytes
	
	
#salts = getBytesFromImages("")

#print(salts)

settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

if len(sys.argv) > 1 and "init" in sys.argv[1].split(","):
	settings["flags"] = ["init"]


print(settings)
vm = VideoMixer(settings)

while True:
	x = vm.run()
	if not x:
		break
	
#vm.run("i")
