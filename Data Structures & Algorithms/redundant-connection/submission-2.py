class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d={}
        for edge in edges :
            if edge[0] in d:
                d[edge[0]].add(edge[1])
            else :
                d[edge[0]]={edge[1]}
            if edge[1] in d:
                d[edge[1]].add(edge[0])
            else :
                d[edge[1]]={edge[0]}
        visited=set()
        def dfs(key,par):
            visited.add(key)
            for x in d[key] :
                if x==par :
                    continue
                if x in visited :
                    continue
                if par in d[x] :
                    visited.remove(key)
                    return True
                else:
                    if dfs(x,par):
                        visited.remove(key)
                        return True
            visited.remove(key)
            return False
        for i in range(len(edges)-1,-1,-1) :
            if dfs(edges[i][1],edges[i][0]) :
                return edges[i]