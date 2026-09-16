class TimeMap:
    """
    store multiple values for the same key at different time stamps
    - can retrieve the key's value at a certain timestamp
    key, timestamp gives us a value

    are timestamps alwasy gonna be increasing?
    yes for set

    for get no

    so we could do 

    set k1, v1, 1
    set k1, v2, 2
    get k1, 4 = v2
    set k1, v3, 4
    get k1, 4 = v3
    get k1, 3 = v2


    dictionary 
    (key)(timestamp) -> value


    get:
    if timestamp matches a time in the data structure, we can just return that time?

    """

    def __init__(self):
        self.store = defaultdict(list)
        

    # stores the key with value at given timestamp
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    # returns a value from key, where the timestamp(t_prev) is <= timestamp
    # if there are multiple values, returns the value associated with the largest t_prev
    # O (log n)
    # we can first try to get key, timestamp 
    # if not we can do binary search 
    # when would we go up, when would we go down?? 
    # the range we would need to check is (1,timestamp)
    # timestamp = 8
    # timestamps, 1, 2, 3, 5, 7, 
    # how would we get 7
    # 4 = dne 
    # go up and down??? 
    # or
    # check up first if theres nothing then we check down 
    # 0 = timestamp
    # 1 = value
    def get(self, key: str, timestamp: int) -> str:
        max_timestamp = -1
        def bin_search(l, r):
            nonlocal max_timestamp
            if l > r:
                return
            m = l + (r-l)// 2
            time, val = self.store[key][m]
            if time  > timestamp:
                bin_search(l, m-1)
            else:
                max_timestamp = m
                bin_search(m +1, r)

        bin_search(0, len(self.store[key])- 1)
        if max_timestamp == -1:
            return ""
        return self.store[key][max_timestamp][1]
