
from pytube import YouTube
from tkinter import *

window = Tk()
window.geometry("700x350")
window.title("#January10miniprojectchallenge")  

text = StringVar()

res1 = IntVar()
res2 = IntVar()
res3 = IntVar()

def downloader():
    global res
    t = text.get()  
    video = YouTube(t)

    if res1.get() == 18:
        res = 18
    elif res2.get() == 22:
        res = 22
    elif res3.get() == 37:
        res = 37

    video_streams = video.streams.filter(file_extension='mp4').get_by_itag(res)
    video_streams.download(filename="Untitled", output_path="video_path")
    Label(window, text="Downloaded Successfully").pack()

Label(window, text="DOWNLOAD YOUTUBE VIDEO", bg='yellow', font=('Calibri 15')).pack()  
Label(window, text="ENTER THE LINK", font=('Calibri 12')).pack() 
Entry(window, textvariable=text, width=50).pack()
Checkbutton(window, text='360p', onvalue=18, offvalue=0, variable=res1).pack()
Checkbutton(window, text='720p', onvalue=22, offvalue=0, variable=res2).pack()
Checkbutton(window, text='1080p', onvalue=37, offvalue=0, variable=res3).pack()

Button(window, text="Download", bg='red', command=downloader).pack()

window.mainloop()
