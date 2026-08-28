# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # minheap
        heap = []
        dummy = ListNode()
        start = dummy
        ctr = 0
        for head in lists:
            if head:
                heap.append((head.val, ctr, head))
            ctr += 1
        heapq.heapify(heap)

        while heap:
            val, cc, node = heapq.heappop(heap)
            ctr += 1
            start.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, ctr, node.next))
            start = start.next


        return dummy.next
