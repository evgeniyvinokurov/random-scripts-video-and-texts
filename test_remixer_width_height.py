import json
from lib.remixer import ReMixer
from lib.randomio import RandomIO

settings = {}
with open("./.config", "rb") as f:
	settings = json.loads(f.read())

settings["8ball"] = True
settings["song"] = True

print(settings)
rem = ReMixer(settings)

folder = "/media/evgenii/TOSHIBA EXT/zhenya/zhszh/"
# v = "/media/evgenii/TOSHIBA EXT/zhenya/zhszh//2023/01/videos/hor/20230123_225633.mp4"

# x = rem.probe(v)
# y = rem.probe_moviepy(v)
# z = rem.ffprobe(v)

# print(x)
# print(y)
# print(z)

# print(x == y)
# print(x == z)
# print(y == z)

# print("------")


files = RandomIO.files(folder, [".mp4"])
count = 0
for file in files:
	print(file)
	try:
		x = rem.probe(file)
		y = rem.probe_moviepy(file)
		z = rem.ffprobe(file)
		
		print(x)
		print(y)
		print(z)

		print(x == y)
		print(x == z)
		print(y == z)
		
		print("------")
		print(str(count))
		
		count = count + 1
		if z != y:
			print("break")
			break
	except:
		print("error")
		print("------ " + str(count))
		count = count + 1
		


#rem.run("i")
