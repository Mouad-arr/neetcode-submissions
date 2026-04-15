class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i,n=0,len(intervals)
        intervals.sort(key=lambda x: x[0])
        while i<n-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.remove(intervals[i+1])
                n=len(intervals)
            else:
                i+=1
        return intervals