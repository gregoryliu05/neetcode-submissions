"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
conflict:
0,7
6,10

0,10
14,16
9,13

0,10
9,13 
14,16 
(0,10), (14,16)
(9,13)
0,30
10,20
15,25

1,5
2,6
3,7
4,8
5,9
by sorting, if the curr meeting doesn't overlap with the prev one, then all subsequent meetings won't overlap with it either
that way, 
how do we allocate days though?
if cur overlap with prev, then we add a day 

if two meetings have a conflict - we have to add a day
- what if we add a day, how do we know if a new interval conflicts with both days?
- we should sort the intervals
    that way we don't have to deal with like going back and checking previous intervals
    for example, we have 5,7 then we have 9,16 then check 6,9
    - it would be hard to go have to go back and confirm 6,9 overlaps with 5,7 or not

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i.start)


        res = 1
        prev = None
        groupEnds = []
        for i in intervals:
            if not prev:
                prev = i
                groupEnds.append(i.end)
                continue
            ps, pe = prev.start, prev.end
            cs, ce = i.start, i.end
            if cs < pe:
                if groupEnds and cs >= groupEnds[0]:
                    end = heapq.heappop(groupEnds)
                    heapq.heappush(groupEnds, max(end, ce))
                else:
                    res += 1
                    heapq.heappush(groupEnds, ce)
            prev = i

        return res
        