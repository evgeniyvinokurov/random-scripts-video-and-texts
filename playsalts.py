import os
import hashlib
from textwrap import wrap

from lib.eightball import EightBall

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
	
image1 = "/pathtoimg1"
image2 = "/pathtoimg2"

musicfolder = "/music1"



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
	      
def getBytesFromImage(pathToImage):	
	sums = getmd5(pathToImage)
	wrapped = wrap(sums, 4)	
	string_bytes = " ".join(wrapped)			
	return string_bytes
		
def music(folder):
	return files(musicfolder, [".mp3", ".MP3"])

musics = music(musicfolder)

#salt_bytes = getTextBytesFromTextDir(folder)


salt_bytes1 = getBytesFromImage(image1)
e81 = EightBall(salt_bytes1)
one = e81.getOneByEightBall(musics)
print(one)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

