import os
import hashlib
from textwrap import wrap
import random
import ffmpeg
import re
import numpy 

from lib.eightball import EightBall
from lib.randomio import RandomIO


################################# INPUTS

textsdir = "./textsdir/"

##################################
		


salt_bytes1 = RandomIO.getTextBytesFromTextDir(textsdir)
e81 = EightBall(salt_bytes1)

texts = salt_bytes1
words = re.split('\s|,|\.|\(|\)|\!', texts)

rewords = ["1"]
rewords2 =["1"]

for word in words:
    num = e81.getOneByEightBall(words, True)	
    word2 = words.pop(num)
	
    num2 = e81.getOneByEightBall(rewords, True)
	
    count = 0
	        
    for word3 in rewords:
        rewords2.append(word3)
        count = count + 1
		
        if count == num2:
            rewords2.append(word2)
    
    rewords = rewords2
    rewords2 = ["1"]

result = " ".join(rewords)

result2 = result.split("1")

ar = []
result3 = []

for res in result2:
    if res.strip() != "":
        ar.append(res)

        if len(ar) > 2:
            result3.extend(ar)
            ar = []
            
result4 = " ".join(result3)

outfile = "./retext" + str(e81.getOneByEightBall(range(1,100000))) + ".txt" 
with open(outfile, mode="w", encoding="utf-8") as f:
	f.write(result4)
	
print("wanna ask? (Y - for auto / text - enter / n - for No)")
quue = input()


while quue != "n":
	num3 = e81.getNumber(len(result3), quue)

	answer = ""	
	if (quue == "Y"):
		num3 = e81.getOneByEightBall(result3, True)

	fornum = e81.getOneByEightBall(range(1,20))

	for i in range(1,fornum):
		answer = answer + " " + result3.pop(num3)
		num3 = num3 - 1
	
	print(answer)
	
	print("")
	print("")
	print("wanna ask? (Y - for auto / text - enter / n - for No)")
	quue = input()

	
print("------------------------------------------------")
print("success")
print("------------------------------------------------")

