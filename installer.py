"""
I will make this installer with tkinter and it 
will basically install the command and add it to
the path env vars automatiocally. 

"""
# from os import system
from tkinter import Tk, Label, Button
from tkinter.constants import S


class installer(Tk):
    def __init__(self):
        super().__init__()
        self.title('moo Installer')
        self.configure(background='white')
        self.main()
        self.geometry('400x100')
    def main(self):
        self.btt = Button(self, text='install',bd=0, fg='white', bg='black', font='sans-serif',  padx=10, pady=10)
        self.btt.pack(padx=20, pady=10)
    def install():
        pass


installer1 = installer()
installer1.mainloop()