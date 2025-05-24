import os
import hashlib
from textwrap import wrap

from lib.eightball import EightBall
from lib.randomio import RandomIO
	
image1 = "/home/evgenii/Desktop/dir/"
musicfolder = "/home/evgenii/Desktop/music folder/"


RUSSIAN = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split(" ")
ENGLISH = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")


#salt_bytes = getTextBytesFromTextDir(folder)


salt_bytes1 = RandomIO.getBytesFromImages(image1)
e81 = EightBall(salt_bytes1)

i = 100
rletter = ""
while i != 0:
	one = e81.getOneByEightBall(RUSSIAN)
	if one:
		rletter = rletter + one
	isendofword = e81.getOneByEightBall([True, False, False, False])
	if isendofword:
		rletter = rletter + " "
	i = i - 1
	
salt_bytes1 = RandomIO.getBytesFromImages(image1)
e82 = EightBall(salt_bytes1)

i = 100
eletter = ""
while i != 0:
	one = e82.getOneByEightBall(ENGLISH)
	if one:
		eletter = eletter + one
		
	isendofword = e81.getOneByEightBall([True, False, False, False])
	if isendofword:
		eletter = eletter + " "
		
	i = i -1
		
print(eletter)
print(rletter)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

