from lib.eightball import EightBall
from lib.randomio import RandomIO
from lib.musicle import Musicle


musicfolder = "C:\\Users\\RobotComp.ru\\Desktop\\testwav"
dirplaylists = "C:\\Users\\RobotComp.ru\\Desktop\\"

# folder with images or texts, at least > than 10 (*.jpgs) or txts with htmls as utf-8
# images = "C:\\Users\\RobotComp.ru\\Desktop\\testimg\\"
txts = "C:\\Users\\RobotComp.ru\\Desktop\\testtxts\\"

# or 
# salt_bytes1 = RandomIO.getBytesFromImages(images)

salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)
e81 = EightBall(salt_bytes1)

print("input count of songs:")
n = int(input())

Musicle.playlist(musicfolder, dirplaylists, n, False, True)

		
print("------------------------------------------------")
print("success")
print("------------------------------------------------")