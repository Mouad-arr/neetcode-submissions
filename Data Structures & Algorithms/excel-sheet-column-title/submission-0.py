class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <27 :
            return chr(64+columnNumber)
        else :
            return self.convertToTitle(columnNumber//26)+chr(64+columnNumber%26)