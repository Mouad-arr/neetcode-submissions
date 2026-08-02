class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,m=len(s)-1,0
        while i>=0 and s[i]==' ':
            i-=1
        while i>=0 and s[i]!= ' ':
            i-=1
            m+=1
        return m