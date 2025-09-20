import sys
from lib.usefull import Usefull

params = []
flags = []

# example terminal: python finder.py .jpg,.txt move
if len(sys.argv) > 1:
    params = sys.argv[1].split(',')
    
if len(sys.argv) > 2:
    flags = sys.argv[2].split(',')


dir = "C:\\Users\\RobotComp.ru\\Desktop\\all"

# where to move duplicates
# didn't exist
dup = "C:\\Users\\RobotComp.ru\\Desktop\\all\\dups"


Usefull.duplicates(params, flags, dir, dup)