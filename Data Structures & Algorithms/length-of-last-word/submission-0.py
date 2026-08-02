class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,m=0,0
        n=len(s)
        while i<n :
            while i<n and s[i]==' ' :
                i+=1
            if i==n :
                break
            m=0
            while i<n and s[i]!=' ' :
                m+=1
                i+=1
        return m
        
            