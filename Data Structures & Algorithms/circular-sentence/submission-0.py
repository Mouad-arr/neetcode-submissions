class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n=len(sentence)
        if sentence[0] != sentence[-1]:
            return False
        i=0
        while i<n :
            if sentence[i]==' ':
                if sentence[i-1]!=sentence[i+1]:
                    return False
            i+=1
        return True
