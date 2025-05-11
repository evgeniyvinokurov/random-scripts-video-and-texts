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
	
image1 = "."
musicfolder = "."


RUSSIAN = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split(" ")
ENGLISH = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")


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
	
def getBytesFromImages(folder):	
	images = files(folder, [".jpg"])
	string_bytes = ""
	
	for i in images:
		sums = getmd5(i)
		wrapped = wrap(sums, 5)	
		string_bytes += " "+(" ".join(wrapped))
	
	return string_bytes
			
def music(folder):
	return files(musicfolder, [".mp3", ".MP3"])


#salt_bytes = getTextBytesFromTextDir(folder)


salt_bytes1 = getBytesFromImages(image1)
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
	
salt_bytes1 = getBytesFromImages(image1)
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

