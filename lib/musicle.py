import os
import hashlib
import shutil
import ffmpeg
import random

class Musicle:
    @staticmethod
    def library(folder, found):  
        exts = Musicle.get_exts()

        try:
            os.makedirs(found)
        except:
            pass
        return Musicle.files(folder, exts)
    
    @staticmethod
    def get_exts():
        return [".mp3", ".MP3", ".flac", ".ogg", ".FLAC", ".OGG", ".wav", ".WAV"]

    @staticmethod
    def files(path, exts) :
        hashes = []
        result = []

        for file in os.listdir(path):
            newpath = path + "/" + file
            try:
                if not os.path.isfile(newpath):	
                    result.extend(Musicle.files(newpath, exts))
            except:
                pass
            for ext in exts:
                try:
                    if os.path.isfile(newpath) and newpath.endswith(ext):
                        result.append(newpath)
                        print("found " + newpath)
                        Musicle.checkfile(newpath, hashes)
                except:
                    pass
        return result

    @staticmethod
    def getmd5(path) :
        try:
            with open(path, "rb") as f:
                bytes = f.read()
                return hashlib.md5(bytes).hexdigest();
        except: 
            pass

    @staticmethod
    def checkfile(m, hashes):
        h = Musicle.getmd5(m)   
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
    
    @staticmethod
    def playlist(musicfolder, dirplaylists, n, e81, passbroken):
        count = 0
        choosen = []

        musics = Musicle.files(musicfolder, Musicle.get_exts())

        while count < n:
            if not e81:
                one = random.choice(musics)
                name = str(random.choice(range(1,100000)))
            else:
                one = e81.getOneByEightBall(musics)
                name = str(e81.getOneByEightBall(range(1,100000)))

            print(one)
            
            if one not in choosen:
                choosen.append(one)
                count = count + 1                

        musicplaylistfile = dirplaylists + name + ".m3u" 

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
        
                