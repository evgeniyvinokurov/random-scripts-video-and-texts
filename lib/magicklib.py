import os
import hashlib
from textwrap import wrap
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
