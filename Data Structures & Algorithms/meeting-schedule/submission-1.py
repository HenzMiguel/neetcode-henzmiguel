"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        prev = None
        for interval in intervals:
            if prev == None:
                prev = interval
                continue
            
            if prev.start <= interval.start < prev.end:
                return False
            elif prev.start <= interval.end < prev.end:
                return False
            
            prev = interval
        return True