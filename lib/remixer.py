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
from .musicle import Musicle
from .usefull import Usefull
from .randomio import RandomIO

class ReMixer:
	def __init__(self, opts):
		print(opts)

		self.opts = opts
		defaults = { "flags": ["all", "both"], "countv": 20, "seconds": [0.2,0.5,0.7,1,1.5,1.7,2,3] }
		
		self.countv = defaults["countv"]
		if "countv" in opts:
			self.countv = opts["countv"]		
			
		self.seconds = defaults["seconds"]
		if "seconds" in opts:
			self.seconds = opts["seconds"]
			
		self.flags = defaults["flags"]	
		if "flags" in opts:
			self.flags = opts["flags"]
		
		self.folders = opts["folders"]
		self.mfolders = opts["mfolders"]

		if "thissong" in opts:
			self.thissong = opts["thissong"]	

		if "song" in opts:
			self.song = True
		
		if "salts" in opts:
			self.e8 = EightBall(opts["salts"])
			self.mode = "salted"			
		elif "8ball" in opts:
			self.e8 = EightBall()
			self.mode = "8ballfree"
		else:
			self.mode = "free"
		
	def run(self):
		print(self.flags)

		finalfile = "./splits/prod/final.mp4"

		try:
			if 'cut' in self.flags:
				self.maketree(['cuts'])
				self.split_files()

			if self.song: 
				self.maketree(['cuts', 'prod', 'temp'])

				while True:
					song = self.get_song(None)
					print(song)
					x = input()
					if x == "y": 
						break  

				self.split_files_to_clip_length(song["duration"])
				self.clear_small_files()
				self.concatenate(finalfile)
				self.make_song(finalfile, song["file"])
				return True

			if "thissong" in self.flags: 
				self.maketree(['cuts', 'prod', 'temp'])
				song = self.get_song(self.thissong)

				self.split_files_to_clip_length(song["duration"])
				self.clear_small_files()
				self.concatenate(finalfile)
				self.make_song(finalfile, song["file"])

			if 'all' in self.flags:
				self.maketree(['cuts', 'prod', 'temp'])
				self.split_files()
				self.clear_small_files()
				self.concatenate(finalfile)
				self.add_audio(finalfile)

			if 'i' in self.flags:
				file_path = Path(finalfile)
				if file_path.exists():
					self.add_audio(finalfile)
				else:
					self.maketree(['prod', 'temp'])
					self.concatenate(finalfile)
					self.add_audio(finalfile)
				

			if 'j' in self.flags:
				self.maketree(['prod', 'temp'])
				self.concatenate(finalfile)
				self.add_audio(finalfile)

			if 'final' in self.flags:
				self.add_audio(finalfile)


		except:
			print("LOGIC ERROR")
			return False
		return True

	# makes tree for files
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

	# all the extensions of possible videos
	def get_exts(self):
		return [".mp4", ".MP4", ".avi", ".AVI", ".mov", ".MOV", ".mkv", ".MKV", ".flv", ".FLV", ".wmv", ".WMV", ".mpg", ".MPG", ".MPG", ".mpeg", ".MPEG", ".m4v", ".M4V", ".VOB", ".vob"]

	# clear_small_filess cuts dir for bad vids cuts
	def clear_small_files(self):	
		video = glob.glob("./splits/cuts/*.mp4")
		for f in video:
			size = os.path.getsize(f)
			if (size < 9000):
				os.remove(f)
	
	# gets files for cuts
	def get_files(self, folder):
		return RandomIO.files(folder, self.get_exts())

	# gets time
	def get_time(self, seconds, dur = 1):
		result = []		
		print(seconds)
		
		begin = self.local_random_range(0, seconds)
		
		print(begin)
		print("begin")
		
		result.append([begin, begin + dur])

		if (seconds is None):
			return False

		return result
		result = str.replace(")","")
		result = result.replace("(","")
		result = result.replace("'","")
		return result.replace(" ", "")	

	# makes splits
	def split_files(self):
		filesofvideos = []

		for folder in self.folders:
			filesofvideos.extend(RandomIO.files(folder, self.get_exts()))

		print(str(len(filesofvideos)) + " videos found")

		i = 0

		while i < self.countv:
			self.make_one_split(filesofvideos)
			i = i + 1

	def split_files_to_clip_length(self, duration):
		filesofvideos = []

		for folder in self.folders:
			filesofvideos.extend(RandomIO.files(folder, self.get_exts()))

		print(str(len(filesofvideos)) + " videos found")

		clip_time = 0

		while clip_time < duration:
			clip_time += self.make_one_split(filesofvideos)

	# choosing random algorithm
	def local_random(self, arr):
		if len(arr) > 0:			
			if(self.mode == "8ballfree"):
				return self.e8.getOneRandomWithEightBall(arr)
			elif(self.mode == "salted"):
				return self.e8.getOneByEightBall(arr)
			else:
				return random.choice(arr)
		return False

	# choosing shuffle algorithm
	def local_shuffle(self, arr):	
		return self.e8.shuffle(arr, self.mode)
	
	# choosing random range algorithm
	def local_random_range(self, minv, maxv):
		return self.e8.randomFromRange(minv, maxv, self.mode)
		
	# makes split from file
	def make_one_split(self, videos):
		while(True):
			file = self.local_random(videos)
			print(file)
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

					if (cond1 or cond5):
						print("dimensionsHorizontal - video is horizontal")
					else:
						if (cond2 or cond4):
							print("dimensionsVertical - video is vertical")
						elif(cond3):
							print("dimensionsBoth - casing both")

					resolved_dimensions = cond1 or cond2 or cond3 or cond4 or cond5

					time = self.get_time(clip.duration, self.local_random(self.seconds))
					pathoforiginal = Path(clip.filename)

					if resolved_dimensions and (time is not False):
						print("dimensionsOk")
						print(time)

						randomTitle = str(self.local_random_range(0, 10000))
						filename = "./splits/cuts/" + randomTitle + "-" + Usefull.remove_spaces(pathoforiginal.name) + "-cut.mp4"

						if "test" not in self.flags:
							try:
								print(filename)
								vid = ffmpeg.input(file)
								vid = vid.trim(start = time[0][0], end = time[0][1]).setpts('PTS-STARTPTS')
								output = ffmpeg.output(vid, filename)
								output.run()
								print("ffmpeg done")
								return time[0][1] - time[0][0]
							except:
								print("ERROR FFMPEG FILE")
								return 0
						else:
							print("test mode")
							return 0
			except:
				print("ERROR MOVIEPY FILE")
				return 0

	# gets audio and combines final clip with audio
	def add_audio(self, finalfile) :
		with VideoFileClip(finalfile) as clip:
			filesofmusic = []

			for folder in self.mfolders:
				filesofmusic.extend(Musicle.music_files(folder))

			print(str(len(filesofmusic)) + " music files found")
			
			try:
				while True:
					file = self.local_random(filesofmusic)
					if Musicle.checkfile_nocopy(file):
						break
					
				print(file)
				tempfile = "./splits/prod/sound.wav"
				audio_input = ffmpeg.input(file)
				audio_cut = audio_input.audio.filter('atrim', duration=clip.duration)
				audio_output = ffmpeg.output(audio_cut, tempfile)
				ffmpeg.run(audio_output)
				print("audio trimmed")

				video = ffmpeg.input(finalfile)
				audio = ffmpeg.input(tempfile)
				audiobasename = Usefull.remove_spaces(os.path.basename(file))
				ffmpeg.concat(video, audio, v=1, a=1).output('./splits/final_' + datetime.now().strftime("%d.%m.%Y_%H:%M:%S") + audiobasename + '.mp4').run()
				print("audio added")
			except:
				print("ERROR AUDIO")
				pass

	# makes audio to video
	def make_song(self, finalfile, song) :
		try:
			video = ffmpeg.input(finalfile)
			audio = ffmpeg.input(song)
			audiobasename = Usefull.remove_spaces(os.path.basename(song))
			ffmpeg.concat(video, audio, v=1, a=1).output('./splits/final_' + datetime.now().strftime("%d.%m.%Y_%H:%M:%S") + audiobasename + '_full_clip.mp4').run()
			print("clip done")
		except:
			print("ERROR AUDIO")
			pass

	# concatentes splits to clip
	def concatenate(self, finalfile):
		try:		
			st = "ffmpeg -i \"concat:"
			alltemp_vids = glob.glob("./splits/cuts/*.mp4")
			file_temp_ts = []
			for f in alltemp_vids:
				file = "./splits/temp/temp" + str(alltemp_vids.index(f) + 1) + ".ts"
				print(f)
				print(file)
				os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
				file_temp_ts.append(file)
			print(file_temp_ts)
			file_temp_ts = self.local_shuffle(file_temp_ts)
			for f in file_temp_ts:
				st += f
				if file_temp_ts.index(f) != len(file_temp_ts)-1:
					st += "|"
				else:
					st += "\" -c copy -bsf:a aac_adtstoasc " + finalfile
			print(st)
			os.system(st)
			print("concatenation done")
		except:
			print("ERROR CONCATENATE")
			pass
	
		# makes split from file
	
	# gets song with length
	def get_song(self, songfile):
		filesofmusic = []
		
		if songfile is None:
			for folder in self.mfolders:
				filesofmusic.extend(Musicle.music_files(folder))

		print(str(len(filesofmusic)) + " music files found")
		
		try:
			while True:
				if songfile is not None:
					file = songfile
				else:
					file = self.local_random(filesofmusic)
					if Musicle.checkfile_nocopy(file):
						break
		except:
			print("ERROR AUDIO")
			pass

		duration = Musicle.file_length(file)
		
		return { "duration": duration, "file": file }
