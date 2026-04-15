class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            if len(s)<=1 :
                return True
            i,j=0,len(s)-1
            while i<j :
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        res,reslen='',0
        n=len(s)
        if n <= 1 :
            return s
        for i in range(n-1):
            for j in range(i+1,len(s)+1):
                if isPalindrome(s[i:j]) :
                    if reslen<len(s[i:j]) :
                        reslen=len(s[i:j])
                        res=s[i:j]
        return res