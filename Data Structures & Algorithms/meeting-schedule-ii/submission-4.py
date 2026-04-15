"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key = lambda x:x.start)
        i,n=1,len(intervals)
        L=[intervals[0].end]
        while i<n:
            if intervals[i].start < L[0]:
                L.append(intervals[i].end)
            else:
                L[0]=max(intervals[i].end,L[0])
            L.sort()
            i+=1
        return len(L)
        