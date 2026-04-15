class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        D={}
        visited=[False for _ in range(numCourses)]
        res=[]
        for p in prerequisites :
            if p[0] in D :
                D[p[0]].add(p[1])
            else :
                D[p[0]]={p[1]}
        def dfs(key) :
            if visited[key] :
                return
            visited[key]=True
            for x in D[key] :
                if x in D and not visited[x] and x not in res :
                    dfs(x)
                    if x not in res :
                        return 
                elif x not in D and x not in res :
                    res.append(x)
                elif x in res :
                    continue
                else:
                    return
            res.append(key)
        for key in D :
            dfs(key)
            if key not in res :
                return []
        for i in range(numCourses) :
            if i not in res :
                res.append(i)
        return res