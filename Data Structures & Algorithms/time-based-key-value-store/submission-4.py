class TimeMap:
    '''
    key1, val1, 1
    key1, val2, 3
    key1, val3, 5

    key1, 4 -> val2
    0, 4 -> mid = 2 
    2 doesn't exist so what do I do then? does that matter?

    if 2 does exist, then we can eliminate bottom half right and 
    search for top 


    how can i do a bin search over the timestamps? (like eliminate 1 half)

    '''

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0 
        r = len(self.store[key]) -1
        max_stamp_index = -1
        while l <= r:
            mid = l + (r-l)//2
            val, nt = self.store[key][mid]
            if nt > timestamp:
                r = mid - 1
            else: 
                max_stamp_index = mid
                l = mid + 1
        if max_stamp_index >= 0:
            return self.store[key][max_stamp_index][0]
        return ""



        
    
        
