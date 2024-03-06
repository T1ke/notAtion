
def getNotationList():
    with open("notationlist.txt", 'r') as f:
        list = f.read().lower()
    return list


class NotationChecker():
    def __init__(self):
        self.notations = getNotationList()
        
    def formatString(self, receivedEntry):
        NotationsSeparated = receivedEntry.split(" ") # separated by a whitespace make proper check eventually 
        for item in NotationsSeparated:
            n = item.split(",")

            if not self.checkNotationProper(n):
                return ""
        return NotationsSeparated

    def checkNotationProper(self,inputList):
        for item in inputList:
            if item.lower() not in self.notations:
                return False
        return True        
