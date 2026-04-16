class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result=[]
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]-intervals[i][0] > intervals[j][1]-intervals[j][0] :
                    interval=intervals[i]
                    intervals[i]=intervals[j]
                    intervals[j]=interval
        for query in queries :
            for i in range(len(intervals)):
                if intervals[i][1]>= query and intervals[i][0]<= query :
                    result.append(intervals[i][1]-intervals[i][0]+1)
                    break
                elif i==len(intervals)-1:
                    result.append(-1)
        return result