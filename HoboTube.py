import pytube

url = 'https://www.youtube.com/watch?v=Ygqpf9ezveo'
youtube = pytube.YouTube(url)

#Descarga video sin sonido
def videoDownload():
    video = youtube.streams.filter(adaptive=True).first().download(output_path='Output/TempFiles', filename='VideoHQ')

#Descarga video low quality
def audioDownload():
    video = youtube.streams.filter(progressive=True).first().download(output_path='Output/TempFiles', filename='Sound')

#Descarga video lq y hq en el directorio /TempFiles
audioDownload()
videoDownload()
