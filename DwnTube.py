#Imports
import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt
import threading
import time

#Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")    ###

#Functions
def download():
    try:
        ytLink = entLink.get()
        ytObj = yt(ytLink, on_progress_callback=progress)
        ytVid = ytObj.streams.get_highest_resolution()
        
        # create a new thread to download the video
        download_thread = threading.Thread(target=ytVid.download)
        download_thread.start()
        
        lblStatus.configure(text="Downloading...")
        
        # check the download progress every 500 milliseconds
        while download_thread.is_alive():
            pbDownload.update()
            root.update()
            time.sleep(0.5)
            lblStatus.update()
            
        lblStatus.configure(text="Finished Downloading")
    except:
        print("Not a valid link!")
        lblStatus.configure(text="Not a Valid Link")


def progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytesDownloaded = size - bytes_remaining
    percentage = bytesDownloaded / size
    pbDownload.set(percentage)
    per = str(int(percentage*100))
    lblStatus.configure(text="Downloading..."+per+'%')

#GUI
root = ctk.CTk()
root.geometry("720x480")
root.title("DwnTube")

lblTitle = ctk.CTkLabel(root, text="Insert a YouTube link:")
lblTitle.pack()

ytUrl = tk.StringVar()
entLink = ctk.CTkEntry(root, width=400, textvariable=ytUrl)
entLink.pack()

lblStatus = ctk.CTkLabel(root, text="")
lblStatus.pack()

pbDownload = ctk.CTkProgressBar(root, width=400)
pbDownload.set(0)
pbDownload.pack() 

btnDownload = ctk.CTkButton(root, text="Download Video", command=download)
btnDownload.pack()

#Show
root.mainloop()