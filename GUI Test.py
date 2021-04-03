from tkinter import *
from PIL import ImageTk, Image

#Base
root = Tk()
root.title('HoboTube')
root.resizable(width=False, height=False)
root['bg'] = '#ffffff'
icon = PhotoImage(file='img/Icon2.png')
root.iconphoto(False, icon)

## I m a g e s ##
#Logo Resize
LogoImgInput = Image.open('img/Logo.png')
LogoImgRe = LogoImgInput.resize((700, 170), Image.ANTIALIAS)
LogoImg = ImageTk.PhotoImage(LogoImgRe)
PatternImg = PhotoImage(file='img/Pattern.png')

#GUI Variables
Logo = Label(root, image=LogoImg, relief='flat', borderwidth=0, width=700, height=170)
VideoDownloaderTag = Label(root, text='-Video downloader-', font=('Comfortaa', 36), bg='#ffffff', fg='#404040', relief='flat')
Pattern = Label(root, image=PatternImg, bg='#ffffff')
LinkEntry = Entry(root, borderwidth=5, font=('Comfortaa', 25), bg='#E5E5E5', fg='#000000', relief='flat', width=40)

#GUI Placement
Logo.grid(column=0, row=1, pady=25, padx=50)
VideoDownloaderTag.grid(column=0, row=2, pady=0, padx=50)
Pattern.grid(column=0, row=3, pady=25)
LinkEntry.grid(column=0, row=4, pady=20, padx=50)




root.mainloop()