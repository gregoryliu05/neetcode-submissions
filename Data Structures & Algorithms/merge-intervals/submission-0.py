class Solution:
    """
    prev, curr

    overlapping 
    (1,3), (2,5)
    (1,3), (1,2)
    (1,3), (3,6)
    (1,3), (3,1)
    overlapping if prev E >= cur S 
    new int = min()
    (5,3), (1,2)


    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        prev = intervals[0]
        for i in intervals:
            ps, pe = prev
            s,e = i
            if pe >= s:
                prev = [min(ps,s), max(pe, e)]
            else:
                res.append(prev)
                prev = i


        res.append(prev)
        return res