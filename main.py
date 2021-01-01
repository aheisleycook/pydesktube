from pytube import YouTube 
import tkinter as tk
from tkinter import messagebox
import os
class Mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        pass
        self.geometry("400x200")
        self.menu = tk.Menu(self)
        self.DIR_DOWNLOAD = os.listdir("downloads")
        self.config(menu=self.menu)
        self.menu.add_command(label="quit", command=self.destroy)
        self.menu.add_command(label="quit", command=self.loadcurrent)
        self.lblTitle = tk.Label(self,text="PyWebTube",relief="raised")
        self.lblTitle.grid(row=3,column=2)
        self.lblurlmsg= tk.Label(self,text="please enter a valid url ")
        self.lblurlmsg.grid(row=3,column=2)
        self.txturl = tk.Entry(self, relief="sunken",)
        self.txturl.grid(column=2,row=4)
        self.btnDownload = tk.Button(self,text="download",command=self.Download)
        self.btnDownload.grid(row=3,column=3)
        self.completedList = tk.Listbox(self)
        self.completedList.grid(row=5,column=6)
        
    def loadcurrent(self):
          for file in self.DIR_DOWNLOAD:
            self.completedList.insert(0,file)


        
    def Download(self):
        try:
            YouTube(self.txturl.get()).streams.first().download("downloads")
            for file in self.DIR_DOWNLOAD:
                self.completedList.insert(0,file)
        except Exception as e:
            messagebox.showerror("error requesting","text you entered is not a valid id")


       
       

app = Mainwindow()
app.mainloop()

