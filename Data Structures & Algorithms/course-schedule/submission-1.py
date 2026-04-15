class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ligne,cols=len(prerequisties),len(prerequisties[0])
        isTaken=[False for _ in range(numCourses)]
        visited=[False for _ in range(numCourses)]
        if len(prerequisites) ==0 :
            return True
        D={}
        requires=set()
        for i in range(len(prerequisites)) :
            if prerequisites[i][0] in D :
                D[prerequisites[i][0]].add(prerequisites[i][1])
            else :
                D[prerequisites[i][0]]={prerequisites[i][1]}
        def dfs(key):
            visited[key]=True
            requires=D[key]
            for x in requires :
                if x in D and not isTaken[x]:
                    if not visited[x] :
                        dfs(x) 
                        if not isTaken[x]:
                            return
                    else :
                        return 
                else :
                    isTaken[x]=True
            isTaken[key]=True
        for key in D:
            dfs(key)
        for i in range(numCourses):
            if isTaken[i]==False and visited[i]==True :
                return False
        return True