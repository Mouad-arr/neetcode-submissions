class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m=len(s1),len(s2)
        t=len(s3)
        d={}
        if t != n+m :
            return False
        def dfs(i,j,k):
            if (i,j,k) in d :
                return  d[(i,j,k)]
            if k==t:
                if i==n and j==m:
                    return True
                return False
            if i<n and s3[k]==s1[i] :
                if dfs(i+1,j,k+1):
                    d[(i,j,k)]=True
                    return True
            if j<m and s3[k]==s2[j]:
                if dfs(i,j+1,k+1) :
                    d[(i,j,k)]=True
                    return True
            d[(i,j,k)]=False
            return False
        return dfs(0,0,0)