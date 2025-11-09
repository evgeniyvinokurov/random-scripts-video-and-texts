import json

from textwrap import wrap
from lib.remixer import ReMixer

settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

settings["8ball"] = True
settings["song"] = True

print(settings)
rem = ReMixer(settings)
x = rem.run()	

#rem.run("i")
