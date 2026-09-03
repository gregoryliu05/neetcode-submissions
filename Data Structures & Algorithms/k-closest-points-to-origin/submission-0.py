import math
class Solution:
    """
    [-2,-4], [-6,-3], [1,4] k =2 
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, [x,y]))

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        