from lib.randomio import RandomIO
from lib.magicklib import MagickLib

# folder with images or texts, at least > than 10 (*.jpgs) or txts with htmls as utf-8
# images = "C:\\Users\\RobotComp.ru\\Desktop\\testimg\\"
txts = "C:\\Users\\RobotComp.ru\\Desktop\\testtxts\\"

# or 
# salt_bytes1 = RandomIO.getBytesFromImages(images)

salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)
res = MagickLib.autoletter(salt_bytes1)

print(res["eletter"])
print("------------------------------------------------")
print(res["rletter"])
print("------------------------------------------------")


