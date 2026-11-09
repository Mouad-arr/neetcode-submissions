class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        res=[]
        cur=list(s[:len(p)])
        p=list(p)
        p.sort()
        i=0
        while i<=len(s)-len(p):
            good=True
            cur.sort()
            for j in range(len(p)):
                if cur[j]!=p[j]:
                    good=False
                    break
            if good :
                res.append(i)
            i+=1
            cur=list(s[i:len(p)+i])
        return res

