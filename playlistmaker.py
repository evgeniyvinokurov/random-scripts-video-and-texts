import os
import hashlib
from textwrap import wrap
import random
import ffmpeg

from lib.eightball import EightBall


################################# INPUTS

textsdir = "./textsdir/"
musicfolder = "/home/evgenii/Desktop/music folder/"
passbroken = True
salts8ballmode = True

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
		
def music(folder):
	return files(folder, [".mp3", ".MP3"])



salt_bytes1 = getTextBytesFromTextDir(textsdir)
e81 = EightBall(salt_bytes1)
count = 0

choosen = []
more = []

print("input count of songs:")
n = int(input())


musics = music(musicfolder)


while count < n:
	if salts8ballmode:
		one = e81.getOneByEightBall(musics)
	else:
		one = random.choice(musics)	
	if one not in choosen:
		choosen.append(one)
		count = count + 1

		
print("------------------------------------------------")
print(choosen)
print("------------------------------------------------")


musicplaylistfile = "./" + str(e81.getOneByEightBall(range(1,100000))) + ".m3u" 


with open(musicplaylistfile, mode="w", encoding="utf-8") as f:
	for m in choosen:	
		if passbroken:
			try:
				ffmpeg.input(m).output("null", f="null").run()
				f.write(m + "\r\n")
			except:
				pass
		else:
			f.write(m + "\r\n")

print(musicplaylistfile)