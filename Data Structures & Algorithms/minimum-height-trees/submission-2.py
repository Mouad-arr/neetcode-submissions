class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1 :
            return [0]
        mp={}
        for edge in edges :
            if edge[0] in mp:
                mp[edge[0]].add(edge[1])
            else:
                mp[edge[0]]={edge[1]}
                if len(mp[edge[0]])==n-1 and n>2:
                    return [edge[0]]
            if edge[1] in mp:
                mp[edge[1]].add(edge[0])
                if len(mp[edge[1]])==n-1 and n>2:
                    return [edge[1]]
            else:
                mp[edge[1]]={edge[0]}
        res={}
        visited={}
        def dfs(root):
            visited[root]=True
            h=0
            for v in mp[root]:
                if v not in visited or not visited[v] :
                    h=max(h,dfs(v)+1) 
            return h
        m=+float('inf')
        for root in mp.keys():
            visited={}
            res[root]=dfs(root)
            m=min(m,res[root])
        l=[]
        for root , val in res.items():
            if val==m:
                l.append(root)
        return l