#Imports
import tkinter as tk #GUI
import customtkinter as ctk #Custom Widgets for GUI
import yt_dlp #Youtube API
import urllib.request #Working with URL's
from PIL import Image, ImageTk #Image editing
import pytube

#Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


class App:
    
    def __init__(self, master):
        #Set Up Form
        self.master = master
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.master.title("DwnTube")
        #Load Widgets
        self.loadMainGUI()
        self.loadYoutubeInfo()
        self.loadVideoInfo()
    def loadMainGUI(self):
        self.lblLink = ctk.CTkLabel(self.master, width= 500, text="Enter a Youtube Link:", font=("Montserrat", 16))
        self.lblLink.place(x=110, y=200)

        self.entLink = ctk.CTkEntry(self.master, width= 400)
        self.entLink.place(x=110, y=240)

        self.btnCont = ctk.CTkButton(self.master, text="->", width=100, command=self.btnCont_onClick)
        self.btnCont.place(x=510, y=240)
    def loadVideoInfo(self):
        self.frmRes = ctk.CTkFrame(self.frmDownload, width= 325, height= 300)
        self.frmRes.place(x= 10, y= 10)

        self.txtDescription = ctk.CTkTextbox(self.frmInfo, wrap=tk.WORD, width= 325, height=140)
        self.txtDescription.place(x=10, y = 200)

        self.btnDownload = ctk.CTkButton(self.frmDownload, text="Download", command=self.download_video)
        self.btnDownload.place(x=100, y=310)
    def loadYoutubeInfo(self):
        self.frmTitle = ctk.CTkFrame(self.master, width= 700, height = 60)
        self.frmTitle.place(x=10, y=490)

        self.lblTitle = ctk.CTkLabel(self.frmTitle, width= 500, font=("Montserrat", 16))
        self.lblTitle.place(x=100, y=5)

        self.lblChannel = ctk.CTkLabel(self.frmTitle, width= 500, font=("Montserrat", 12))
        self.lblChannel.place(x=100, y=30)

        self.frmInfo = ctk.CTkFrame(self.master, width= 345, height= 350)
        self.frmInfo.place(x= 10, y= 520)

        self.frmDownload = ctk.CTkFrame(self.master, width= 345, height= 350)
        self.frmDownload.place(x= 365, y= 520)

        self.lblThumbnail = ctk.CTkLabel(self.frmInfo, text="")
        self.lblThumbnail.place(x=10, y=10)

    def btnCont_onClick(self):
        self.get_yt_video_info()
        self.animateUp()

    def animateUp(self):
        # Move the widgets upward
        for i in range(24):
            self.lblLink.place(y=200-i*10)
            self.entLink.place(y=240-i*10)
            self.btnCont.place(y=240-i*10)
            self.frmTitle.place(y=480-i*10)
            self.frmInfo.place(y=550-i*10)
            self.frmDownload.place(y=550-i*10)
            self.master.update()
            self.master.after(20)
        for i in range(20):
            self.frmTitle.place(y=240-i*10)
            self.frmInfo.place(y=310-i*10)
            self.frmDownload.place(y=310-i*10)
            self.master.update()
            self.master.after(20)
    def get_yt_video_info(self):
        # Set the video URL
        global video_url
        video_url = self.entLink.get()
        # Create a yt-dlp object
        ydl = yt_dlp.YoutubeDL()
        # Extract the video information
        global video_info
        video_info = ydl.extract_info(video_url, download=False)
        # Get the video title
        video_title = video_info.get('title', None)
        video_description = video_info.get('description', None)
        video_thumbnail = video_info.get('thumbnail', None)
        channel_name = video_info.get('channel', None)
        # Print the video title
        self.lblTitle.configure(text=video_title)
        self.txtDescription.insert(tk.END, video_description)
        self.lblChannel.configure(text="By: "+channel_name)
        # Download thumbnail image using urllib
        with urllib.request.urlopen(video_thumbnail) as url:
            thumbnail_image = Image.open(url)
        # Convert thumbnail image to Tkinter-compatible format
        thumbnail_tk = ImageTk.PhotoImage((thumbnail_image).resize((320,180),Image.Resampling.NEAREST))
        self.lblThumbnail.configure(image=thumbnail_tk)
        formats = video_info.get("formats", [])

        global selected_resolution 
        selected_resolution = tk.StringVar()
        unique_resolutions = set()
        
        for format in formats:
            if format.get("acodec") != "none":
                rbRes = ctk.CTkRadioButton(self.frmRes, text="Audio Only", variable=selected_resolution, value=format.get("format_id"), width=325)
                unique_resolutions.add("audio only")
                rbRes.pack()
                break
        for format in formats:
            resolution = format.get("resolution","Unknown")
            if resolution not in unique_resolutions:
                unique_resolutions.add(resolution)
                rbRes = ctk.CTkRadioButton(self.frmRes, text=resolution, variable=selected_resolution, value=format.get("format_id"), width=325)
                rbRes.pack()
    def download_video(self):
        yt_dlp.YoutubeDL({'format': "17"}).download([video_url])

# Create the cTkinter application
root = ctk.CTk()
app = App(root)

# Start the main event loop
root.mainloop()