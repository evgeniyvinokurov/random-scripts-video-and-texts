import os
import hashlib
from textwrap import wrap
import random
import ffmpeg

from lib.eightball import EightBall
from lib.randomio import RandomIO


################################# INPUTS

textsdir = "./textsdir/"
musicfolder = "/home/evgenii/Desktop/music folder/"
passbroken = True
salts8ballmode = True

##################################



salt_bytes1 = RandomIO.getTextBytesFromTextDir(textsdir)
e81 = EightBall(salt_bytes1)
count = 0

choosen = []
more = []

print("input count of songs:")
n = int(input())


musics = RandomIO.music(musicfolder)


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