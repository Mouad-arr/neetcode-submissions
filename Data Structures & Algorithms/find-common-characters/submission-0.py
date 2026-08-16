class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars=set(words[0])
        res=[]
        for c in chars :
            good=True
            count=words[0].count(c)
            for i in range(1,len(words)):
                y=words[i].count(c)
                if y == 0 :
                    good=False
                    break
                elif y < count :
                    count = y
            if good :
                res+=[c]*count
        return res