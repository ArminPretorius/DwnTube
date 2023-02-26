#Imports
import tkinter as tk #GUI
import customtkinter as ctk #Custom Widgets for GUI
import yt_dlp #Youtube API
import urllib.request #Working with URL's
from PIL import Image, ImageTk #Image editing

#Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("720x480")
        ##self.master.resizable(False, False)
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

        self.lblDescription = ctk.CTkLabel(self.master, text="test")
        self.lblDescription.place(x=20, y = 800)
    

    def btnCont_onClick(self):
        #self.get_video_info()
        self.animateUp()


    def get_video_info(self):
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
            self.lblDescription.place(y=760-i*10)
            self.master.update()
            self.master.after(20)
        for i in range(20):
            self.lblTitle.place(y=240-i*10)
            self.lblChannel.place(y=270-i*10)
            self.lblThumbnail.place(y=320-i*10)
            self.lblDescription.place(y=520-i*10)
            self.master.update()
            self.master.after(20)

# Create the cTkinter application
root = ctk.CTk()
app = App(root)

# Start the main event loop
root.mainloop()