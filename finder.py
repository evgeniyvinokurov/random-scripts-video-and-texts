import os
import hashlib
import sys
import shutil

from pathlib import Path

params = sys.argv[1].split(',')
flags = sys.argv[2].split(',')
path = "."
movefiles = False

if len(params) > 0:
	exts = params
else:
	exts = [".jpg"]

if "move" in flags:
	movefiles = True

def getmd5(path) :
	try:
		with open(path, "rb") as f:
			bytes = f.read()
			return hashlib.md5(bytes).hexdigest();
	except: 
		pass

def files(path) :
	result = []
	for file in os.listdir(path):
		newpath = path + "/" + file
		try:
			if not os.path.isfile(newpath):	
				result.extend(files(newpath))
		except:
			pass
		for ext in exts:
			try:
				if os.path.isfile(newpath) and newpath.endswith(ext):
					result.append(newpath)
			except:
				pass
	return result

md5hashes = []
dublicates = []

for file in files("."):
	md5 = getmd5(file)
	if md5 not in md5hashes:
		md5hashes.append(md5)
	else:
		dublicates.append(file)

if movefiles: 
	try:
		os.makedirs("./duplicatesdir")
	except:
		pass
	for file in dublicates:
		f = Path(file)		
		newdir = "./duplicatesdir/" + str(f.parent).replace("./", "")		
		try:
			os.makedirs(newdir)
		except:
			pass
		shutil.move(file, newdir)
else:
	print(dublicates)