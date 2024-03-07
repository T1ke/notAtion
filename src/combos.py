class Combos:
    def __init__(self):
        self.description = ""
        self.moves = []
    
    def addDescription(self, string):
        self.description = string
       

    def addMove(self, move):
        self.moves.append(move)
        
    
    def removeMoveFromCombo(self):
        self.moves.pop(-1)

    def updateComboList(self):
        return self.moves
    

    def printCombo(self):
        print(self.moves)