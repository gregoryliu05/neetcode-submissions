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
        self.store = defaultdict(dict)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        # bin search
        l = 0 
        r = timestamp 
        max_timestamp = 0
        while l <= r:
            if r in self.store[key]:
                return self.store[key][r]
            mid = l + (r-l) // 2
            if mid not in self.store[key]:
                r -= 1
            else:
                max_timestamp = max(max_timestamp, mid)
                l = mid + 1
        
        if max_timestamp in self.store[key]:
            return self.store[key][max_timestamp]
        else:
            return ""
                



        
    
        
