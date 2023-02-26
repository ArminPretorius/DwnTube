#Imports
import tkinter as tk
import customtkinter as ctk
#from pytube import YouTube as yt
import yt_dlp
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO
import threading
import time

#Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

#New Code
class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.master.title("DwnTube")

        #Create a Label widget
        self.lblLink = ctk.CTkLabel(self.master, width= 500, text="Enter a Youtube Link:", font=("Montserrat", 16))
        self.lblLink.place(x=110, y=200)

        # Create an Entry widget
        self.entLink = ctk.CTkEntry(self.master, width= 400)
        self.entLink.place(x=110, y=240)

        # Create a button to trigger the animation
        self.btnCont = ctk.CTkButton(self.master, text="->", width=100, command=self.btnCont_onClick)
        self.btnCont.place(x=510, y=240)

        # Title Label
        self.lblTitle = ctk.CTkLabel(self.master, width= 500, font=("Montserrat", 16))
        self.lblTitle.place(x=110, y=480)

        # Channel Label
        self.lblChannel = ctk.CTkLabel(self.master, width= 500, font=("Montserrat", 12))
        self.lblChannel.place(x=110, y=480)

        self.lblThumbnail = ctk.CTkLabel(self.master, text="")
        self.lblThumbnail.place(x=20, y=560)

        self.lblDescription = ctk.CTkLabel(self.master, text="")
        self.lblThumbnail = ctk.CTkLabel(self.master, text="")
        self.lblThumbnail.place(x=20, y=560)
    

    def btnCont_onClick(self):
        self.get_video_title()
        self.animateUp()


    def get_video_title(self):
        # Set the video URL
        video_url = self.entLink.get()
        # Create a yt-dlp object
        ydl = yt_dlp.YoutubeDL()
        # Extract the video information
        video_info = ydl.extract_info(video_url, download=False)
        # Get the video title
        video_title = video_info.get('title', None)
        video_description = video_info.get('description', None)
        video_thumbnail = video_info.get('thumbnail', None)
        channel_name = video_info.get('channel', None)
        # Print the video title
        self.lblTitle.configure(text=video_title)
        print(video_description)
        print(video_thumbnail)
        self.lblChannel.configure(text="By: "+channel_name)
        # Download thumbnail image using urllib
        with urllib.request.urlopen(video_thumbnail) as url:
            thumbnail_image = Image.open(url)
        # Convert thumbnail image to Tkinter-compatible format
        thumbnail_tk = ImageTk.PhotoImage((thumbnail_image).resize((384,216),Image.Resampling.NEAREST))
        self.lblThumbnail.configure(image=thumbnail_tk)

    def animateUp(self):
        # Move the widgets upward
        for i in range(24):
            self.lblLink.place(y=200-i*10)
            self.entLink.place(y=240-i*10)
            self.btnCont.place(y=240-i*10)
            self.lblTitle.place(y=480-i*10)
            self.lblChannel.place(y=510-i*10)
            self.lblThumbnail.place(y=560-i*10)
            self.master.update()
            self.master.after(20)
        for i in range(20):
            self.lblTitle.place(y=240-i*10)
            self.lblChannel.place(y=270-i*10)
            self.lblThumbnail.place(y=320-i*10)
            self.master.update()
            self.master.after(20)

# Create the cTkinter application
root = ctk.CTk()
app = App(root)

# Start the main event loop
root.mainloop()


#Old Code
##Settings
#ctk.set_appearance_mode("System")
#ctk.set_default_color_theme("dark-blue")    ###
#
##Functions
#def download():
#    try:
#        ytLink = entLink.get()
#        ytObj = yt(ytLink, on_progress_callback=progress)
#        ytVid = ytObj.streams.get_highest_resolution()
#        
#        # create a new thread to download the video
#        download_thread = threading.Thread(target=ytVid.download)
#        download_thread.start()
#        
#        lblStatus.configure(text="Downloading...")
#        
#        # check the download progress every 500 milliseconds
#        while download_thread.is_alive():
#            pbDownload.update()
#            root.update()
#            time.sleep(0.5)
#            lblStatus.update()
#            
#        lblStatus.configure(text="Finished Downloading")
#    except:
#        print("Not a valid link!")
#        lblStatus.configure(text="Not a Valid Link")
#
#
#def progress(stream, chunk, bytes_remaining):
#    size = stream.filesize
#    bytesDownloaded = size - bytes_remaining
#    percentage = bytesDownloaded / size
#    pbDownload.set(percentage)
#    per = str(int(percentage*100))
#    lblStatus.configure(text="Downloading..."+per+'%')
#
##GUI
#root = ctk.CTk()
#root.geometry("720x480")
#root.title("DwnTube")
#
#lblTitle = ctk.CTkLabel(root, text="Insert a YouTube link:")
#lblTitle.pack()
#
#ytUrl = tk.StringVar()
#entLink = ctk.CTkEntry(root, width=400, textvariable=ytUrl)
#entLink.pack()
#
#lblStatus = ctk.CTkLabel(root, text="")
#lblStatus.pack()
#
#pbDownload = ctk.CTkProgressBar(root, width=400)
#pbDownload.set(0)
#pbDownload.pack() 
#
#btnDownload = ctk.CTkButton(root, text="Download Video", command=download)
#btnDownload.pack()
#
##Show
#root.mainloop()