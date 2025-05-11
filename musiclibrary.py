import os
import hashlib
import shutil
import ffmpeg
from moviepy.editor import AudioFileClip

hashes = []

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
					print("found " + newpath)
					checkfile(newpath)
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

def checkfile(m):
    h = getmd5(m)   
    if h not in hashes:
        try:
            ffmpeg.input(m).output("null", f="null").run()
            hashes.append(h)
            basename = os.path.basename(m)
            print(basename)
            shutil.copyfile(m, "./found/" + basename)  
            print("copyed " + m)
        except:
            print("damaged " + m)
            pass	
		
def music(folder):
	return files(folder, [".mp3", ".MP3", ".flac", ".ogg", ".FLAC", ".OGG"])


musicfiles = music(".")
# print(musicfiles)

