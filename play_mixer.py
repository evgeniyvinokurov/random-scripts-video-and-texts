import hashlib
import os
import json
import sys

from textwrap import wrap
from lib.mixer import VideoMixer

	
settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

if len(sys.argv) > 1 and "init" in sys.argv[1].split(","):
	settings["flags"] = ["init"]


print(settings)
vm = VideoMixer(settings)

while True:
	x = vm.run()
	if not x:
		break
	
#vm.run("i")
