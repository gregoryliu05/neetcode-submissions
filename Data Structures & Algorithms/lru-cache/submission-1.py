class ListNode:
    def __init__(self, key, value, nxt = None, prv = None):
        self.key = key
        self.value = value
        self.prev = prv
        self.next = nxt
    def __str__(self):
        return f"{self.key}, {self.value}, {self.prev}, {self.next}"

class LRUCache:
    """
    use = get or put
    key value pairs


    """

    def __init__(self, capacity: int):
        self.size = 0
        self.maxsize = capacity
        self.cache = dict()
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail # lru at the head
        self.tail.prev = self.head # mru at the tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        # add to end 
        self.add_end(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) 
            self.size -= 1

        if self.size == self.maxsize:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
            self.size -= 1
            # create new
        newNode = ListNode(key, value)
        self.cache[key] = newNode
        # add to end 
        self.add_end(newNode)
        self.size += 1
    
    def remove(self, node) -> ListNode:
        # head ->  2 <-> tail
        nxt = node.next # 2
        prv = node.prev # head
        nxt.prev = prv
        prv.next = nxt
        return node
        
        
    
    def add_end(self, node) -> None:
        # head <-> tail
        # head <-> node <-> tail
        prv = self.tail.prev # head
        self.tail.prev = node 
        node.next = self.tail
        node.prev = prv
        prv.next = node 
        
        
        
