import os
import hashlib
from textwrap import wrap
import re

from lib.eightball import EightBall
from lib.randomio import RandomIO

class MagickLib:	
    RUSSIAN = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split(" ")
    ENGLISH = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
   
    @staticmethod
    def autoletter(saltsbytes) :
        e81 = EightBall(saltsbytes)

        i = 100
        rletter = ""
        while i != 0:
            one = e81.getOneByEightBall(MagickLib.RUSSIAN)
            if one:
                rletter = rletter + one
            isendofword = e81.getOneByEightBall([True, False, False, False])
            if isendofword:
                rletter = rletter + " "
            i = i - 1
            
        e82 = EightBall(saltsbytes)

        i = 100
        eletter = ""
        while i != 0:
            one = e82.getOneByEightBall(MagickLib.ENGLISH)
            if one:
                eletter = eletter + one
                
            isendofword = e81.getOneByEightBall([True, False, False, False])
            if isendofword:
                eletter = eletter + " "
                
            i = i -1
            
        return { "eletter":  eletter, "rletter": rletter}        

    @staticmethod
    def livequery(textsdir):        
        texts = RandomIO.getTextBytesFromTextDir(textsdir)
        e81 = EightBall(texts)        
        
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

    @staticmethod
    def lottery(n, L, e81):
        count = 0
        choosen = []

        numbers = range(1,L)

        while count < n:
            one = e81.getOneByEightBall(numbers)
            if one not in choosen:
                choosen.append(one)
                count = count + 1

        return choosen	
