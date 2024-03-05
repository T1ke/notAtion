from tkinter import Tk, ttk

import Images.Notations as N




def getNotationList():
    with open("notationlist.txt", 'r') as f:
        list = f.read().lower()
    return list


class Window(Tk):
    def __init__(self):
        self.notations = getNotationList()
        super().__init__()
        style1 = ttk.Style()
        style1.configure("BW.TLabel", foreground="black", background="white")

        self.title("Tekken notation window")

        self.EntryBox = ttk.Entry(text="Test", style="BW.TLabel")
        self.inputBtn = ttk.Button(text="add Notation")
        self.inputBtn.bind("<Button>", self.inputBtnFunction)
        self.EntryBox.pack()
        self.inputBtn.pack()

    def checkNotationProper(self,inputList):
        for item in inputList:
            if item.lower() not in self.notations:
                return False
        return True
    

    def inputBtnFunction(self, event):
        EntryText = self.EntryBox.get()
        NotationsSeparated = EntryText.split(" ") # separated by a whitespace make proper check eventually

        if not self.checkNotationProper(NotationsSeparated):
            print("Wrong input!")
            return
        
        print(NotationsSeparated)

