class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        if n<3:
            return 0
        if n==3 :
            if s[0]==s[-1]:
                return 1
            return 0
        L = [[-1, -1] for _ in range(26)]
        for i in range(n):
            if L[ord(s[i])-ord('a')][0]==-1:
                L[ord(s[i])-ord('a')][0]=i
            L[ord(s[i])-ord('a')][1]=i
        res=0
        for pairs in L:
            if pairs[0]<pairs[1]:
                res+= len(set(s[pairs[0]+1:pairs[1]]))
        return res
