class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        c=0
        def dfs(i,j,cur) :
            nonlocal c                   
            if i>=n or j>=m:
                return 
            if s[i]==t[j]:
                cur.append(t[j])
                if len(cur)==m :
                    c+=1
                else:
                    dfs(i+1,j+1,cur)
                cur.pop()
                dfs(i+1,j,cur)
            else:
                dfs(i+1,j,cur)
        dfs(0,0,[])
        return c  