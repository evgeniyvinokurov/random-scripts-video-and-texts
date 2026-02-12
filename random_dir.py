import random

from lib.usefull import Usefull
# from lib.magicklib import MagickLib
from lib.eightball import EightBall

dir = "/media/evgenii/TOSHIBA EXT"

print("enter salts:")
salts = str(input())


with open('dirs.txt', 'r') as f:
    dirs = f.readlines()
        
# print(dirs)
count = 5
one_dir = ""
e81 = EightBall(salts)

while True:
    if len(dirs) > 0:
        one_dir = e81.getOneByEightBall(dirs)
    else:
        dirs = Usefull.find_all_dirs(dir)              
        one_dir = e81.getOneByEightBall(dirs)
        
        # one_dir = random.choice(dirs)

        with open('dirs.txt', 'w') as f:
            for i in dirs:
                f.write(i + '\r\n')

    print(one_dir)

    count = count - 1
    if count == 0:
        break

