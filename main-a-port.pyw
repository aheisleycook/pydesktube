from pytube import YouTube 
import tkinter as tk
from tkinter import messagebox
import os
class Mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        pass
        self.geometry("400x400")
        #self.iconbitmap("pwt.ico")
        self.menu = tk.Menu(self, background="lightblue")
        self.title("pydesktube") 
        self.resizable(0,0)
        self.DIR_DOWNLOAD = os.listdir("Downloads")
        self.config(menu=self.menu)
        self.menu.add_command(label="quit", command=self.destroy)
        self.menu.add_separator()
        self.lblTitle = tk.Label(self,text="PyWebTube", background="blue", foreground="yellow", relief="raised")
        self.lblTitle.grid(row=1,column=2)
        self.lblurlmsg= tk.Label(self,text="please enter a valid url ")
        self.lblurlmsg.grid(row=0,column=3)
        self.txturl = tk.Entry(self, relief="sunken",)
        self.txturl.grid(column=3,row=0)
        self.btnDownload = tk.Button(self,text="download", background="blue",command=self.Download)
        self.lbllistTitle = tk.Label(self,text="complated   video downlaodes")
        self.lbllistTitle.grid(row=2,column=2)
        self.btnDownload.grid(row=0,column=2)
        self.completedList = tk.Listbox(self) 
        self.completedList.grid(row=3,column=2)
        self.lblStatus = tk.Label
        #this allwos you copy id easye
        #self.bind("<Button-2>",self.pastUrl)
        self.bind("<Button-3>",self.loadcurrent)


      
        
        
    def loadcurrent(self,action):
        self.completedList.delete(0)
        for file in self.DIR_DOWNLOAD:
            self.completedList.insert(0,file)
    def pastUrl(self,action):
        self.txturl.insert(0,pyperclip.paste())


        
    def Download(self):
        try:
            YouTube(self.txturl.get()).streams.first().download("downloads")
            for file in self.DIR_DOWNLOAD:
                self.completedList.insert(0,file)
        except Exception as e:
            messagebox.showerror("error requesting","text you entered is not a valid id")

    def fileDownload(self,action):
        try:
            YouTube(self.txturl.get()).streams.first().download("downloads")
            for file in self.DIR_DOWNLOAD:
                self.completedList.insert(0,file)
        except Exception as e:
            messagebox.showerror("error requesting","text you entered is not a valid id")
       
       

app = Mainwindow()
app.mainloop()
