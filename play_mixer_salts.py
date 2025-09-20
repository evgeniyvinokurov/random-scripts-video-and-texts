import hashlib
import os
import json
import sys

from textwrap import wrap
from lib.mixer import VideoMixer
from lib.randomio import RandomIO

################################# INPUTS

textsdir = "./textsdir/"

##################################



salt_bytes1 = RandomIO.getTextBytesFromTextDir(textsdir)

settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

settings["salts"] = salt_bytes1

if len(sys.argv) > 1 and "init" in sys.argv[1].split(","):
	settings["flags"] = ["init"]

print(settings)
vm = VideoMixer(settings)


while True:
	x = vm.run()
	if not x:
		break
#vm.run("i")
