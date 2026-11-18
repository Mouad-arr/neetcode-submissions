class Solution:
    def partitionString(self, s: str) -> int:
        se=set()
        n=len(s)
        count=0
        for i in range(n):
            if s[i] in se :
                count+=1
                se={s[i]}
            else:
                se.add(s[i])
        return count +1