class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        if n<=10:
            return []
        se=set()
        res=set()
        i=0
        while i+10<=n:
            string=s[i:i+10]
            if string in se :
                res.add(string)
            else:
                se.add(string)
            i+=1
        return list(res)
