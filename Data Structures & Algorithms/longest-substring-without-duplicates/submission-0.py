class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s=list(s)
        M=0
        lastOne=[]
        for S in s :
            if S not in lastOne:
                lastOne.append(S)
                M=max(M,len(lastOne))
            else :
                i=lastOne.index(S)
                if i==len(lastOne)-1:
                    lastOne=[]
                else:
                    lastOne=lastOne[i+1:]
                lastOne.append(S)
        return M
