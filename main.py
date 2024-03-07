from src.GUI import Window 
from src.notationChecker import NotationChecker
from src.imageGenerator import ImageGenerator
from src.combos import Combos


def main():
    n = NotationChecker()
    im = ImageGenerator()
    c = Combos
    window = Window(n, im, c)
    window.geometry("500x500")
    window.resizable(width=False, height=False)
    #window.maxsize(width=1000, height=1000)
    #window.minsize(width=300, height=300)
    window.mainloop()


def getNotationsFromFiles(): ## 
    import os
    notations = []

    for f in os.listdir("Images/Notations"):
        if f.endswith(".png"):
            notation = os.path.splitext(f)[0]
            notations.append(notation)
    print(notations)


    

if __name__ == "__main__":
    main()
    #getNotationsFromFiles()