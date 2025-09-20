from lib.eightball import EightBall
from lib.randomio import RandomIO
from lib.magicklib import MagickLib

# folder with images or texts, at least > than 10 (*.jpgs) or txts with htmls as utf-8
# images = "C:\\Users\\RobotComp.ru\\Desktop\\testimg\\"
textsdir = "C:\\Users\\RobotComp.ru\\Desktop\\testtxts\\"

# salts strings
salt_bytes1 = RandomIO.getTextBytesFromTextDir(textsdir)

# or 
# salt_bytes1 = RandomIO.getBytesFromImages(images)

# way to deal with choosing
e81 = EightBall(salt_bytes1)


print("L. input last number in sequence from 1..L (ALL NUMBERS): ")
L = int(input())

print("n. input count of digits (COUNT TO CHOOSE FROM 1..L):")
n = int(input())

choosen = MagickLib.lottery(n, L, e81)
		
print("------------------------------------------------")
print(choosen)
print("------------------------------------------------")


