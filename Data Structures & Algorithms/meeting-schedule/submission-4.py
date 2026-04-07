"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)
        prev = None

        for interval in intervals:
            if prev == None:
                prev = interval
                continue
            
            if prev.end > interval.start:
                return False
            
            prev = interval
        return True