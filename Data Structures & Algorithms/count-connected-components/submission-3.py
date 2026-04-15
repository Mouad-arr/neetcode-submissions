class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:   
        D={}
        for p in edges : 
            if p[0] not in D :
                D[p[0]]={p[1]}
            else :
                D[p[0]].add(p[1])
            if p[1] not in D :
                D[p[1]]={p[0]}
            else :
                D[p[1]].add(p[0])
        visited=set()
        N=0
        def dfs(n) :
            visited.add(n)
            for x in D[n] :
                if x in D and x not in visited :
                    dfs(x)
                else :
                    visited.add(x)
            return
        for key in D :
            if key not in visited :
                dfs(key)
                N+=1 
        return N+n-len(visited)