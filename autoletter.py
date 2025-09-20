from lib.randomio import RandomIO
from lib.magicklib import MagickLib

# folder with images or texts, at least > than 10 (*.jpgs) or txts with htmls as utf-8
# image1 = "C:\\Users\\RobotComp.ru\\Desktop\\testimg\\"
txts = "C:\\Users\\RobotComp.ru\\Desktop\\testtxts\\"

# or 
# salt_bytes1 = RandomIO.getBytesFromImages(image1)

salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)
res = MagickLib.autoletter(salt_bytes1)

print(res["eletter"])
print("------------------------------------------------")
print(res["rletter"])
print("------------------------------------------------")


