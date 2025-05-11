import ffmpeg
from moviepy.editor import VideoFileClip

videofile = "./python-scripts-in.mp4"
audiofile = "./TalesFromTheCrypt.mp3"
videofileout = "./python-scripts-out.mp4"

with VideoFileClip(videofile) as clip:
	audio_input = ffmpeg.input(audiofile)
	audio_cut = audio_input.audio.filter('atrim', duration=clip.duration)
	audio_output = ffmpeg.output(audio_cut, audiofile + "-test.mp3")
	ffmpeg.run(audio_output)

	video = ffmpeg.input(videofile)
	audio = ffmpeg.input(audiofile+"-test.mp3")
	ffmpeg.concat(video, audio, v=1, a=1).output(videofileout).run()

