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


textsdir = "./textsdir/"

salt_bytes1 = getTextBytesFromTextDir(textsdir)
e81 = EightBall(salt_bytes1)
count = 0

choosen = []
more = []

print("input count of digits:")
n = int(input())

print("input last number in sequence from 1..:")
L = int(input())

numbers = range(1,L)

print(e81.getOneByEightBall(numbers))

while count < n:
    one = e81.getOneByEightBall(numbers)
    if one not in choosen:
        choosen.append(one)
        count = count + 1

		
print("------------------------------------------------")
print(choosen)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

