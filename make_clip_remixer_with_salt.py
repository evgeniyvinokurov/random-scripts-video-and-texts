import json

from lib.remixer import ReMixer
from lib.randomio import RandomIO


settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

txts = "./textsdir/"
salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)

settings["salts"] = salt_bytes1
settings["song"] = True

rem = ReMixer(settings)
x = rem.run()	

#rem.run("i")
