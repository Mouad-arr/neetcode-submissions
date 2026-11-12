class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        if n<=k :
            return False
        f=set()
        sub=s[:k]
        f.add(int(sub,2))
        i=k
        while i<n:
            sub=sub[1:]+s[i]
            i+=1
            f.add(int(sub,2))
        return len(f)==2**k