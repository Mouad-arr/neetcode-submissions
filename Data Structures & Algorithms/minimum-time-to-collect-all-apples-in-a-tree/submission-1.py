class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if len(edges)==0:
            return 0
        tree={}
        for edge in edges :
            if edge[0] not in tree :
                tree[edge[0]]=[edge[1]]
            else :
                tree[edge[0]].append(edge[1])
            if edge[1] not in tree :
                tree[edge[1]]=[edge[0]]
            else :
                tree[edge[1]].append(edge[0])
        visited=[False]*(n+1)
        def func(i):
            visited[i]=True
            if hasApple[i]:
                if i==0:
                    ans=0
                else :
                    ans=2
                for e in tree[i]:
                    if not visited[e]:
                        (pas,good)=func(e)
                        if good :
                            ans+=pas
                return (ans,True)
            else:
                if i==0:
                    ans=0
                else :
                    ans=2
                for e in tree[i]:
                    if not visited[e]:
                        (pas,good)=func(e)
                        if good :
                            ans+=pas
                if ans > 2:
                    return (ans,True)
                return (0,False)
        (ans,t)=func(0)
        return ans