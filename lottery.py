import os
import hashlib
from textwrap import wrap

from lib.eightball import EightBall
from lib.randomio import RandomIO

textsdir = "./textsdir/"

salt_bytes1 = RandomIO.getTextBytesFromTextDir(textsdir)
e81 = EightBall(salt_bytes1)
count = 0

choosen = []
more = []

print("input count of digits:")
n = int(input())

print("input last number in sequence from 1..:")
L = int(input())

numbers = range(1,L)

print(e81.getOneByEightBall(numbers))

while count < n:
    one = e81.getOneByEightBall(numbers)
    if one not in choosen:
        choosen.append(one)
        count = count + 1

		
print("------------------------------------------------")
print(choosen)
print("------------------------------------------------")


#salt_bytes2 = getBytesFromImage(image2)
#e82 = EightBall(salt_bytes2)
#two = e82.getOneByEightBall(musics)
#print(two)

#print("------------------------------------------------")

