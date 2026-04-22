from lib.remixer import ReMixer
from lib.randomio import RandomIO

settings = {	
	"folders": ["/home/evgenii/2023","/home/evgenii/2024","/home/evgenii/2025", "/media/evgenii/TOSHIBA EXT/zhenya/zhszh", "/media/evgenii/85799339-6cf7-41b9-902d-ac6601c1dc21/2026"],	
	"mfolders": ["/home/evgenii/Desktop/all/before work/music folder/"],
	"seconds": [1, 1.5, 1.7, 2,3, 4.2, 4.6],	
	"flags": ["horizontal", "song", "8ball"]
}

txts = "./textsdir/"
salt_bytes1 = RandomIO.getTextBytesFromTextDir(txts)

settings["salts"] = salt_bytes1

rem = ReMixer(settings)
x = rem.run()	

#rem.run("i")
