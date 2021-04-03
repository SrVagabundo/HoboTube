import os
from moviepy.editor import *


#Coje el video LQ y lo pasa a mp3
def convertMP3():
    video = VideoFileClip(os.path.join("Output/TempFiles/Sound.mp4"))
    video.audio.write_audiofile(os.path.join("Output/Audio.mp3"))


#Coje el video HQ y lo fusiona con el audio anterior
def merge():
    videoHQ = VideoFileClip(os.path.join("Output/TempFiles/VideoHQ.mp4"))
    audioclip = AudioFileClip(os.path.join('Output/Audio.mp3'))
    new_audioclip = CompositeAudioClip([audioclip])
    videoHQ.audio = new_audioclip
    videoHQ.write_videofile(os.path.join('Output/Video.mp4'))

convertMP3()
merge()