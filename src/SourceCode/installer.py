"""
I will make this installer with tkinter and it 
will basically install the command and add it to
the path env vars automatiocally. 
the command to use to set the user vars
setX PATH "C:\Program Files\moo;%PATH%".
"""
# from tests import progressBar
# from os import system



from tkinter import StringVar, Tk, Label, Button
from tkinter.constants import HORIZONTAL
from tkinter.ttk import *
from time import sleep
from os import path, getcwd, mkdir
from os import system
from shutil import copy



class installer(Tk):
    def __init__(self) -> None:
            super().__init__()
            try:
                self.iconbitmap("logo (2).ico")
            except:
                pass
            self.title("Moo installer")
            self.configure(background="#101010")
            # self.resizable(200, 200)
            self.geometry("700x150")
            self.components = list()
            self.prog()
    def appendComponent(self, comp):
        self.components.append(comp)
    def install(self):
        for _ in range(100):
            sleep(0.05)
            self.myPrg['value'] += 1
            if self.myPrg['value'] >= 50:
                if self.myPrg['value'] == 50:
                    path = getcwd()
                    print(path)
                    system(f'setX PATH \"{path}\\dist\\moo\;%PATH%"')
                self.lbl['text'] = '   Updating the user variables...'
                self.update_idletasks()
            self.update_idletasks()
        
        # system("setX PATH \"C:\\Program Files\\moo;%PATH%\"")
        print('set the path var!!')
        for i in self.components:
            i.destroy()
        self.geometry("700x70")
        self.lbl = Label(self, text='Installed successfully!! run the command moo in the terminal to test',font='Helvetica')
        self.lbl.pack(pady=10, ipadx=13, ipady=5)
    def prog(self):
        self.myPrg = Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate")
        self.myPrg.pack(padx=10, pady=10)
        self.appendComponent(self.myPrg)
        self.lbl = Label(self, text='   installing the command...  ',font='Helvetica')
        self.lbl.pack(pady=10, ipadx=13, ipady=5)
        self.appendComponent(self.lbl)  
        self.button = Button(self,text="install",command=self.install)
        self.appendComponent(self.button)
        self.button.pack(pady=10)



installer1 = installer()
installer1.mainloop()