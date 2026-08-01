class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        i=0
        sm=0
        while i<n-1 :
            sm+=abs( ord(s[i])-ord(s[i+1]) )
            i+=1
        return sm