"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    ans is between 1 and n
    n = len(intervals)

    5,10
    8,12
    = 2
    5, 15
    8, 12
    13,15
    """
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)

        # sort by start time
        intervals.sort(key=lambda interval: interval.start)
        min_heap = []
        for i in intervals:
            if not min_heap:
                min_heap.append(i.end)
            else:
                if min_heap[0] <= i.start:
                    heapq.heappop(min_heap)
                heapq.heappush(min_heap, i.end)

                


        return len(min_heap)
        