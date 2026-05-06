"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    how can we say a meeting overlaps?
    1,10
    s1, e1
    s2, e2
    if s2 < e1 while s2 >= s1
    """
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        isi = []
        for i in intervals:
            isi.append([i.start, i.end])
        isi.sort()
        for i in range(1, len(isi)):
            s1, e1 = isi[i-1]
            s2, e2 = isi[i]
            if s2 < e1 and s2 >= s1:
                return False
        return True
        
