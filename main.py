from pytube import YouTube 
import tkinter as tk
from tkinter import messagebox
class Mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        pass
        self.geometry("400x200")
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="quit", command=self.destroy)
        self.lblTitle = tk.Label(self,text="PyWebTube",relief="raised")
        self.lblTitle.grid(row=4,column=4)
        self.lblurlmsg= tk.Label(self,text="please enter a valid url ")
        self.lblurlmsg.grid(row=5,column=4)
        self.txturl = tk.Entry(self, relief="sunken",)


        
    #def Download(self):
     #YouTube.streams.first().download()   
       

app = Mainwindow()
app.mainloop()

