class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindromic(s):
            x=len(s)
            if x<=1 :
                return True
            i,j=0,x-1
            while i<j :
                if s[i]!=s[j] :
                    return False
                i+=1
                j-=1
            return True
        n=len(s)
        if n <= 1 :
            return n 
        count=0
        for i in range(n):
            for j in range(i+1,n+1):
                if isPalindromic(s[i:j]) :
                    count+=1
        return count