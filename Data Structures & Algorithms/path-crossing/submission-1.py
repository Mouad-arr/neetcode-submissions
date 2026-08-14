class Solution:
    def isPathCrossing(self, path: str) -> bool:
        grid={(0,0)}
        cur=(0,0)
        good=False
        for p in path :
            if p == 'S' :
                cur = (cur[0],cur[1]-1)
            elif p == 'N':
                cur = (cur[0],cur[1]+1)
            elif p == 'E' :
                cur = (cur[0]+1,cur[1])
            else :
                cur = (cur[0]-1,cur[1])
            if cur in grid :
                good=True
                break
            grid.add(cur)
        return good
