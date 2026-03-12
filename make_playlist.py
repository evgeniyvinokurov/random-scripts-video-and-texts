from lib.eightball import EightBall
from lib.randomio import RandomIO
from lib.musicle import Musicle


musicfolder = "/home/evgenii/Desktop/all/before work/music folder/"
dirplaylists = "/home/evgenii/Desktop/"

# folder with images or texts, at least > than 10 (*.jpgs) or txts with htmls as utf-8
# images = "C:\\Users\\RobotComp.ru\\Desktop\\testimg\\"
txts = "./textsdir"

# or 
# salt_bytes1 = RandomIO.getBytesFromImages(images)

salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)
e81 = EightBall(salt_bytes1)

print("input count of songs:")
n = int(input())

# Musicle.playlist(musicfolder, dirplaylists, n, False, True)
Musicle.playlist(musicfolder, dirplaylists, n, e81)

		
print("------------------------------------------------")
print("success")
print("------------------------------------------------")