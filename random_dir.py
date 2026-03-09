import random

from lib.randomio import RandomIO
from lib.eightball import EightBall

dir = "/media/evgenii/TOSHIBA EXT"

        
# print(dirs)
count = 5
one_dir = ""
mode = "8balll"
e81 = None
dirs = []

if mode == "8ball":
    print("enter salts:")
    salts = str(input())
    e81 = EightBall(salts)

try:
    with open('dirs.txt', 'r') as f:
        dirs = f.readlines()
except:
    pass

def get(mode, ar):
    if mode == "8ball":               
        return e81.getOneByEightBall(ar)
    else:
        return random.choice(ar)

while True:
    if len(dirs) > 0:
        one_dir = get(mode, dirs)
    else:
        dirs = RandomIO.dirs(dir)       
        # one_dir = random.choice(dirs)

        with open('dirs.txt', 'w') as f:
            for i in dirs:
                f.write(i + '\r\n')            
        one_dir = get(mode, dirs)
    print(one_dir)

    count = count - 1
    if count == 0:
        break

