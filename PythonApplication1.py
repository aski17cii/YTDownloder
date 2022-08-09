from cProfile import label
from email import message
from msilib.schema import Directory
from tkinter import messagebox
from yt_dlp import YoutubeDL
import tkinter
from tkinter import END, Label, PhotoImage, filedialog

def VideoDown():
    if((text1.get("1.0","end-1c") == "" ) or (text2.get("1.0","end-1c") == "")):
        messagebox.showinfo(title="e.g.", message="정보가 부족합니다")
    else:
        URL = text1.get("1.0","end-1c")
        directory = text2.get("1.0","end-1c")
        ydl_opts = {'outtmpl': '{0}/%(title)s.%(ext)s'.format(directory)}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)

def DirectorySearch():
    dir_path = filedialog.askdirectory(parent=window,initialdir="/",title='Please select a directory')
    text2.delete("1.0", END)
    text2.insert("1.0", dir_path)

window = tkinter.Tk()
window.geometry("1000x600+100+100")
window.resizable(False, False)

# 다운로드할 동영상 URL 입력창
label1 = tkinter.Label(window, text="URL을 입력해주세요.")
label1.place(x=30, y=10)
text1 = tkinter.Text(window, width=30, height=2, font=("Arial", 16))
text1.place(x=30, y=30)

#다운로드한 파일 위치 지정
label2 = tkinter.Label(window, text="다운로드할 폴더를 선택하세요", width=40, height=1)
label2.place(x=350, y=10)
button1 = tkinter.Button(window, width=10, height=1, text="파일 선택", bg="#ffffff", command=DirectorySearch)
button1.place(x=600, y=10)
text2 = tkinter.Text(window, width=30, height=1, font=("Arial", 16))
text2.place(x=420, y=40)

#다운로드 버튼
button2 = tkinter.Button(window, width=10, height=1, text="영상 다운로드", bg="#ffffff", command=VideoDown)
button2.place(x=30, y=100)


window.mainloop()




