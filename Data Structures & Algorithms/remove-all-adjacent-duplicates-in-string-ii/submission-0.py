class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n=len(s)
        i=0
        while i<n :
            j=i
            count=1
            while j+1<n and count < k and s[j]==s[j+1]:
                count+=1
                j+=1
            if count==k:
                s=s[:i]+s[j+1:]
                i=0
                n=len(s)
            else:
                i=j+1
        return s