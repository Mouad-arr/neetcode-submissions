class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp={}
        keys=set()
        for p in prerequisites :
            if p[0] not in mp :
                mp[p[0]]={p[1]}
            else:
                mp[p[0]].add(p[1])
            keys.add(p[1])
            if p[1] in mp :
                mp[p[0]].update(mp[p[1]])
            if p[0] in keys:
                for key in mp :
                    if p[0] in mp[key] :
                        mp[key].update(mp[p[0]])

        res=[]
        for q in queries :
            if q[0] not in mp:
                res.append(False)
            elif q[1] in mp[q[0]] : 
                res.append(True)
            else :
                res.append(False)
        return res