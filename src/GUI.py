from tkinter import Tk, ttk
from strings import WRONGFORMAT
from PIL import Image, ImageTk


import Images.Notations as N


class Window(Tk):
    def __init__(self, notationChecker, imageGenerator):
        super().__init__()
        self.notationChecker = notationChecker
        self.imageGen = imageGenerator

        style1 = ttk.Style()
        style1.configure("BW.TLabel", foreground="black", background="white")

        self.title("Tekken notation window")

        self.EntryBox = ttk.Entry(text="Test", style="BW.TLabel")
        self.inputBtn = ttk.Button(text="add Notation")
        self.inputBtn.bind("<Button>", self.transferEntry)
        self.EntryBox.pack()
        self.inputBtn.pack()


    def transferEntry(self, event):
        EntryText = self.EntryBox.get()
        formatNotation = self.notationChecker.formatString(EntryText)
        if len(formatNotation) == 0:
            print(WRONGFORMAT)
            return
        

        self.addNotationImages(formatNotation)
        
    def addNotationImages(self, fn):
        for item in fn:
            imgFile = self.imageGen.getImage(item)
            img = Image.open(imgFile)
            img = img.resize((30,30), Image.ANTIALIAS)

            im = ImageTk.PhotoImage(img)

            img_label = ttk.Label(image=im)
            img_label.image = im
            img_label.pack()

        
