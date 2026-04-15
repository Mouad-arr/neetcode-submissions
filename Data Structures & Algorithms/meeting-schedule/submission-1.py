"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n=len(intervals)
        for i in range(1,n):
            if intervals[i].start < intervals[i-1].end and  intervals[i].start>= intervals[i-1].start :
                return False
        return True