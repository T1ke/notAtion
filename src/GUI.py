from tkinter import Tk, ttk, Toplevel, Canvas, Scrollbar, Frame
from strings import WRONGFORMAT
from PIL import Image, ImageTk


import Images.Notations as N


class Window(Tk):
    def __init__(self, notationChecker, imageGenerator, combos):
        super().__init__()
        self.notationChecker = notationChecker
        self.imageGen = imageGenerator
        self.combos = combos
        self.hitCnt = 0
        self.comboCount = 0
        self.grid_rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        #self.grid_propagate(False)
        self.mainFrame = Frame(self, bg="gray")
        self.mainFrame.grid(sticky="news")
        #self.mainFrame.grid_propagate(False)

        style1 = ttk.Style()
        style1.configure("BW.TLabel", foreground="black", background="white")

        self.title("Tekken notation window")
        self.setMainWindow()

        self.setOutputFrame()
        ################# FRAME



    def setMainWindow(self):
        self.EntryBox = ttk.Entry(self.mainFrame, text="Test", style="BW.TLabel")
        self.EntryBox.grid(row=0, column=0,columnspan=2,sticky="w", rowspan=2, ipadx=3, ipady=3)

        self.inputBtn = ttk.Button(self.mainFrame, text="Add Notation")
        self.inputBtn.bind("<Button>", self.transferEntry)
        self.inputBtn.grid(row=0, column=2, sticky="w", padx=2, pady=2)

        self.clearBtn = ttk.Button(self.mainFrame, text="Clear")
        self.clearBtn.bind("<Button>", self.clear)
        self.clearBtn.grid(row=1, column=2, sticky="w", padx=2, pady=2)

        self.newNotationBtn = ttk.Button(self.mainFrame, text="New combo")
        self.newNotationBtn.bind("<Button>", self.newCombo)
        self.newNotationBtn.grid(row=2, column=2, sticky="w", padx=2, pady=2)

    def setOutputFrame(self):
        self.comboFrame = Frame(self.mainFrame)
        self.comboFrame.grid(row=4, column=0, sticky='nw')
        self.comboFrame.grid_rowconfigure(0, weight=1)
        self.comboFrame.grid_columnconfigure(0, weight=1)    
        #self.comboFrame.grid_propagate(False)

        self.canvas = Canvas(self.comboFrame, bg="black")
        self.canvas.grid(row=0, column=0, sticky="news")
        self.canvas.grid_propagate(False)
        vscrollbar = Scrollbar(self.comboFrame,orient="vertical")
        hscrollbar= Scrollbar(self.comboFrame,orient="horizontal")

        vscrollbar.config(command=self.canvas.yview)
        vscrollbar.grid(row=0, column=1, sticky="ns")

        self.canvas.config(scrollregion=self.canvas.bbox("all"))


    def transferEntry(self, event):
        EntryText = self.EntryBox.get()
        formatNotation = self.notationChecker.formatString(EntryText)
        if len(formatNotation) == 0:
            print(WRONGFORMAT)
            return
        
        self.addNotationImages(formatNotation)

        
    def addNotationImages(self, fn):

        for item in fn:
            self.hitCnt += 1
            imgFile = self.imageGen.getImage(item)
            img = Image.open(imgFile)
            img = img.resize((25,25), Image.ANTIALIAS)
            
            im = ImageTk.PhotoImage(img)
            img_label = ttk.Label(self.canvas, image=im)
            img_label.image = im
            img_label.grid(row=self.comboCount + 4,column=self.hitCnt, sticky="w")
            

    def clear(self, event):
        self.EntryBox.delete(0, 'end')
        

    def newCombo(self, event):
        self.comboCount += 1
        self.hitCnt = 0
        self.EntryBox.delete(0, 'end')
        
