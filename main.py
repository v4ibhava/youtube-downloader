from tkinter import *
from pytube import YouTube


def downloader():
    link = inputtxt.get("1.0", 'end-1c')
    yt = YouTube(link)
    videos = yt.streams.filter(progressive=True)
    vid = list(enumerate(videos))

    output_text = "Available Qualities:\n"
    for i, video in vid:
        output_text += f"{i + 1}. {video.resolution}\n"

    output.config(text=output_text)

    choice_val = input_choice.get("1.0", 'end-1c')
    if choice_val:
        try:
            strm = int(choice_val) - 1
            videos[strm].download()
            download_msg.config(text=f'Your video "{yt.title}" /nhas been downloaded successfully.')
        except ValueError:
            download_msg.config(text='Invalid input. Please enter a valid number.')
    else:
        download_msg.config(text='Please enter a number to choose a video quality.')

root = Tk()
root.title('Youtube Downloader')
cfont = ('Terminal',14)
root.geometry('400x300')

text = Label(root, text="Paste your link down below", fg='Black')
text.pack()
text.config(font=cfont)
inputtxt = Text(root, height=1, width=20)
inputtxt.pack(pady=(10, 10))

output = Label(root, text='', bg='grey', fg='white')
output.pack(pady=(10, 10))

input_choice = Text(root, height=1, width=20)
input_choice.pack(pady=(10, 10))

download_btn = Button(root, text='Download', command=downloader)
download_btn.pack(pady=(10, 10))

download_msg = Label(root, text='', bg='grey', fg='white',height=10)
download_msg.pack(pady=(10, 10))

root.mainloop()
