class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result=[]
        for query in queries :
            r=[]
            for i in range(len(intervals)):
                if intervals[i][1]>= query and intervals[i][0]<= query :
                    r.append(intervals[i][1]-intervals[i][0]+1)
            if len(r)==0:
                result.append(-1)
            else:
                result.append(min(r))
        return result