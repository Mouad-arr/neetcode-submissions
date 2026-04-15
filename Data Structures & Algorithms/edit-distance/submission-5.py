class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2 :
            return 0
        n,m=len(word1),len(word2)
        if min(n,m)==0:
            return max(n,m)
        d={}
        def dfs(i,j):
            res=0
            if (i,j) in d :
                return d[(i,j)]
            if word1[i]==word2[j] :
                if j == m-1 and i == n-1 :
                    return 0
                elif j==m-1 :
                    res += n-i-1
                elif i==n-1 :
                    res+= m-j-1
                else:
                    res+=dfs(i+1,j+1)
            else:
                res+=1
                if i==n-1 and j==m-1 :
                    return res
                elif i==n-1 :
                    res+=min(dfs(i,j+1),m-j-1)
                elif j==m-1 :
                    res+=min(dfs(i+1,j),n-i-1)
                else:
                    res += min(dfs(i,j+1) , dfs(i+1,j) ,dfs(i+1,j+1))
            d[(i,j)]=res
            return res
        return dfs(0,0)