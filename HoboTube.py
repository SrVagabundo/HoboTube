#I'm bored as fuck
import pytube
import os
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from moviepy.editor import CompositeAudioClip
from tkinter import *
from PIL import ImageTk, Image


#Base
root = Tk()
root.title('HoboTube')
root.resizable(width=False, height=False)
root['bg'] = '#ffffff'
icon = PhotoImage(file='img/Icon2.png')
root.iconphoto(False, icon)

############ I m a g e s ############
#Logo Resize
LogoImgInput = Image.open('img/Logo.png')
LogoImgRe = LogoImgInput.resize((805, 205), Image.ANTIALIAS)
LogoImg = ImageTk.PhotoImage(LogoImgRe)
PatternImg = PhotoImage(file='img/Pattern.png')
downloadButtonImg = PhotoImage(file='img/download.png')
disclaimerImg = PhotoImage(file='img/disclaimer.png')

############ U R L   d e l   v i d e o   d e   Y o u T u b e ############
LinkEntry = Entry(root, borderwidth=5, font=('Comfortaa', 25), bg='#E5E5E5', fg='#000000', relief='flat', width=40)

############ F u n c i o n e s   Y o u T u b e ############

#Descarga video high quality
def videoDownload():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(adaptive=True).first().download(output_path='Output/TempFiles', filename='VideoHQ')

#Descarga video low quality
def audioDownload():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(progressive=True).first().download(output_path='Output/TempFiles', filename='Sound')


#Coje el video LQ y lo pasa a mp3
def convertMP3():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    video = VideoFileClip(os.path.join("Output/TempFiles/Sound.mp4"))
    video.audio.write_audiofile(os.path.join("Output/Audio.mp3"))


#Coje el video HQ y lo fusiona con el audio anterior
def mergeHQ():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    videoHQ = VideoFileClip(os.path.join("Output/TempFiles/VideoHQ.mp4"))
    audioclip = AudioFileClip(os.path.join('Output/Audio.mp3'))
    new_audioclip = CompositeAudioClip([audioclip])
    videoHQ.audio = new_audioclip
    videoHQ.write_videofile(os.path.join('Output/Video.mp4'))
    

def merge4K():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    videoHQ = VideoFileClip(os.path.join("Output/TempFiles/VideoHQ.webm"))
    audioclip = AudioFileClip(os.path.join('Output/Audio.mp3'))
    new_audioclip = CompositeAudioClip([audioclip])
    videoHQ.audio = new_audioclip
    videoHQ.write_videofile(os.path.join('Output/Video.mp4')) 


#Si el video es 2K/4K, o solo HD
def DownloadButton():
    LinkInput = LinkEntry.get()
    url = LinkInput
    youtube = pytube.YouTube(url)
    videoDownload()
    audioDownload()
    if os.path.isfile('Output/TempFiles/VideoHQ.mp4')==True:
        convertMP3()
        mergeHQ()
    elif os.path.isfile('Output/TempFiles/VideoHQ.webm')==True:
        convertMP3()
        merge4K()

############ G U I   V a r i a b l e s ############
Logo = Label(root, image=LogoImg, relief='flat', borderwidth=0, width=805, height=205)
VideoDownloaderTag = Label(root, text='-Video downloader-', font=('Comfortaa', 36), bg='#ffffff', fg='#404040', relief='flat')
Pattern = Label(root, image=PatternImg, bg='#ffffff')
downloadButton = Button(root, bg='#ffffff', borderwidth=0, relief='flat', image=downloadButtonImg, command=DownloadButton)
disclaimer = Label(root, image=disclaimerImg, bg='#ffffff')

############ G U I   P l a c e m e n t ############
Logo.grid(column=0, row=1, pady=25, padx=50)
VideoDownloaderTag.grid(column=0, row=2, pady=0, padx=50)
Pattern.grid(column=0, row=3, pady=25)
LinkEntry.grid(column=0, row=4, pady=20, padx=50)
downloadButton.grid(column=0, row=5, pady=35, padx=50)
disclaimer.grid(column=0, row=10, pady=50, padx=50)

root.mainloop()
