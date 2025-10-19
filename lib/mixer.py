import os
import sys
import shutil
import glob
import ffmpeg
import random
import datetime
import time
import random
import json

from datetime import datetime
from pathlib import Path
from moviepy.editor import VideoFileClip
from .eightball import EightBall

class VideoMixer:
	def __init__(self, opts):
		self.opts = opts
		defaults = { "flags": ["all", "both"], "exts": [".mp4"], "countv": 20, "seconds": [0.2,0.5,0.7,1,1.5,1.7,2,3] }
		
		if "countv" in opts:
			self.countv = opts["countv"]
		else:
			self.countv = defaults["countv"]
			
		if "exts" in opts:
			self.exts = opts["exts"]
		else:
			self.exts = defaults["exts"]					
			
		if "seconds" in opts:
			self.seconds = opts["seconds"]
		else:
			self.seconds = defaults["seconds"]
			
		if "flags" in opts:
			self.flags = opts["flags"]
		else:
			self.flags = defaults["flags"]		
		
		self.folders = opts["folders"]
		self.mfolders = opts["mfolders"]

		self.videos = []
		
		
		if "salts" in opts:
			self.e8 = EightBall(opts["salts"])
		else:
			self.e8 = EightBall()

		self.init()
	

	def init(self):
		for folder in self.folders:
			self.videos.extend(self.files(folder, self.exts))

		
	def run(self):
		print(self.flags)
		
		if 'cut' in self.flags:	
			self.maketree(['cuts'])
			self.ffmpegdo()

		if 'all' in self.flags:
			self.maketree(['cuts', 'prod', 'temp'])
			self.ffmpegdo()
			self.clear()
			self.concatenate()
			self.addaudio()

		if 'i' in self.flags:	
			self.maketree(['prod', 'temp'])
			self.clear()
			self.concatenate()
			self.addaudio()

		if 'j' in self.flags:	
			self.maketree(['prod', 'temp'])
			self.concatenate()
			self.addaudio()
			
		if 'final' in self.flags:
			self.addaudio()
		
		return True

	def maketree(self, maketreevars):
		if 'cuts' in maketreevars:
			try:
				shutil.rmtree("./splits/cuts")
			except:
				pass
			try:
				os.makedirs("./splits/cuts")
			except:
				pass

		if 'prod' in maketreevars:
			try:
				shutil.rmtree("./splits/prod")
			except:
				pass
			try:
				os.makedirs("./splits/prod")
			except:
				pass

		if 'temp' in maketreevars:
			try:
				shutil.rmtree("./splits/temp")
			except:
				pass
			try:
				os.makedirs("./splits/temp")
			except:
				pass

	# clears cuts dir for bad vids cuts
	def clear(self):	
		video = glob.glob("./splits/cuts/*.mp4")
		for f in video:
			size = os.path.getsize(f)
			if (size < 10000):
				os.remove(f)

	# gets time 
	def gettime(self, seconds, dur = 1):
		result = []		
		print(seconds)
		
		begin = self.e8.randomFromRange(0, seconds)
		
		print(begin)
		print("begin")
		
		result.append([begin, begin + dur])

		if (seconds is None):
			return False

		return result

	# finds files by exts in dir
	def files(self, path, extss) :
		result = []
		for file in os.listdir(path):
			newpath = path + "/" + file
			try:
				if not os.path.isfile(newpath):	
					result.extend(self.files(newpath, extss))
			except:
				pass
			for ext in extss:
				try:
					if os.path.isfile(newpath) and newpath.endswith(ext):
						result.append(newpath)
				except:
					pass
		return result

	# makes splits from random files in folders with numbers
	def ffmpegdo(self) :	
		print("videos:")
		print(self.videos)
		
		i = 0

		while i < self.countv:
			file = self.e8.random(self.videos)
			try:
				with VideoFileClip(file) as clip:
					size = clip.size

					h = size[1]
					w = size[0]
					
					cond1 = ("/hor" in file) and ("horizontal" in self.flags)
					cond2 = ("/vert" in file) and ("vertical" in self.flags)

					cond4 = (h > w) and ("vertical" in self.flags) and (not "/hor" in file)
					cond5 = (w > h) and ("horizontal" in self.flags) and (not "/vert" in file)	

					cond3 = "both" in self.flags

					print(self.flags)
					print(file)
					print(cond1)					
					print(cond2)					
					print(cond3)
					print(cond4)
					print(cond5)

					resolved_dimensions = cond1 or cond2 or cond3 or cond4 or cond5

					time = self.gettime(clip.duration, self.e8.random(self.seconds))
					pathoforiginal = Path(clip.filename) 									
					if resolved_dimensions and (time is not False):	
						# print("if")
						randomTitle = str(self.e8.randomFromRange(0, 10000))
						# print("random title")
						# print(randomTitle)
						filename = "./splits/cuts/" + str(i) + "-" + randomTitle + "-" + self.removespaces(pathoforiginal.name) + "-cut.mp4"	
						# print(filename)		
						# print("ready")		
						if "test" not in self.flags:
							try:
								print("before input")
								vid = ffmpeg.input(file)	
								# print(vid)
								# print("vid")	
								vid = vid.trim(start = time[0][0], end = time[0][1]).setpts('PTS-STARTPTS')			
								output = ffmpeg.output(vid, filename)
								# print(output)
								# print("output")	
								output.run()
							except:
								print("ffmpeg error")
										
						i = i + 1
			except:
				print("got an error on meta video file")
				pass

	# gets audio and combines final clip with audio
	def addaudio(self) :
		with VideoFileClip("./splits/prod/final.mp4") as clip:
			filesofmusic = []
			for folder in self.mfolders:
				filesofmusic.extend(self.files(folder, [".mp3"]))
			
			test = False
			while not test:
				try:
					file = self.e8.random(filesofmusic)
					audio_input = ffmpeg.input(file)
					audio_cut = audio_input.audio.filter('atrim', duration=clip.duration)
					audio_output = ffmpeg.output(audio_cut, './splits/prod/sound.wav')
					ffmpeg.run(audio_output)
					video = ffmpeg.input('./splits/prod/final.mp4')
					audio = ffmpeg.input('./splits/prod/sound.wav')
					audiobasename = self.removespaces(os.path.basename(file))
					ffmpeg.concat(video, audio, v=1, a=1).output('./splits/final_' + datetime.now().strftime("%d.%m.%Y_%H:%M:%S") + audiobasename + '.mp4').run()
					test = True
				except:
					test = False
					pass

	# concatentes splits to clip
	def concatenate(self):
		vert = ""
		if ("vertical" in self.flags and "hand" in self.flags):
			vert = "/vert"
		elif ("horizontal" in self.flags and "hand" in self.flags):
			vert = "/gor"
		
		st = "ffmpeg -i \"concat:"
		video = glob.glob("./splits/cuts" + vert + "/*.mp4")
		file_temp = []
		for f in video:
			print(f)
			file = "./splits/temp/temp" + str(video.index(f) + 1) + ".ts"
			os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
			file_temp.append(file)
		print(file_temp)
		random.shuffle(file_temp)
		for f in file_temp:
			st += f
			if file_temp.index(f) != len(file_temp)-1:
				st += "|"
			else:
				st += "\" -c copy -bsf:a aac_adtstoasc ./splits/prod/final.mp4"
		print(st)
		os.system(st)

	def removespaces(self, str):
		result = str.replace(")","")
		result = result.replace("(","")
		result = result.replace("'","")
		return result.replace(" ", "")	
	
