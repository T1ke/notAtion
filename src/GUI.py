from tkinter import Tk, ttk
from strings import WRONGFORMAT
from PIL import Image, ImageTk


import Images.Notations as N


class Window(Tk):
    def __init__(self, notationChecker, imageGenerator):
        super().__init__()
        self.notationChecker = notationChecker
        self.imageGen = imageGenerator
        self.rowCount = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        style1 = ttk.Style()
        style1.configure("BW.TLabel", foreground="black", background="white")

        self.title("Tekken notation window")

        self.EntryBox = ttk.Entry(self, text="Test", style="BW.TLabel")
        self.EntryBox.grid(row=0, column=2, sticky="e", padx=5, pady=5)

        self.inputBtn = ttk.Button(self, text="Add Notation")
        self.inputBtn.bind("<Button>", self.transferEntry)
        self.inputBtn.grid(row=1, column=2, sticky="n", padx=5, pady=5)

        self.clearBtn = ttk.Button(self, text="Clear")
        self.clearBtn.bind("<Button>", self.clear)
        self.clearBtn.grid(row=1, column=3, sticky="w", padx=5, pady=5)

        self.newNotationBtn = ttk.Button(text="New combo")
        self.newNotationBtn.bind("<Button>!", self.newCombo)
        self.newNotationBtn.grid(row=self.rowCount+3, column=4, sticky="e")


    def transferEntry(self, event):
        EntryText = self.EntryBox.get()
        formatNotation = self.notationChecker.formatString(EntryText)
        if len(formatNotation) == 0:
            print(WRONGFORMAT)
            return
        
        self.addNotationImages(formatNotation)

        
    def addNotationImages(self, fn):
        cnt = 0
        for item in fn:
            cnt += 1
            imgFile = self.imageGen.getImage(item)
            img = Image.open(imgFile)
            img = img.resize((30,30), Image.ANTIALIAS)

            im = ImageTk.PhotoImage(img)
            img_label = ttk.Label(image=im)
            img_label.image = im
            img_label.grid(row=self.rowCount + 2,column=cnt, sticky="w", padx=2, pady=2)
            

    def clear(self):
        print("hahah ei toimi vielä")
        pass

    def newCombo(self):
        self.rowCount += 1
        pass
