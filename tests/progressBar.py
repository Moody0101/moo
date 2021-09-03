from tkinter import Tk, Button
from tkinter import ttk
from time import sleep
from tkinter.constants import HORIZONTAL

class progress(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Peogress")
        self.configure(background="#101010")
        # self.resizable(200, 200)
        self.geometry("700x100")
        self.prog()
    def install(self):
        for _ in range(100):
            # print(self.myPrg['value'])
            self.myPrg['value'] += 1
            self.update_idletasks()
            sleep(0.1)
    def prog(self):

        self.myPrg = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate")

        self.myPrg.pack(padx=10, pady=10)
        button = Button(self, bd=0,text="install", command=self.install)
        button.pack(pady=10)

prg = progress()
prg.mainloop()
