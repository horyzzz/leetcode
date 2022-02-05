from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode()
        # 二叉堆
        heap = []
        for i, phead in enumerate(lists):
            if phead:
                heappush(heap, (phead.val, i, phead))
        
        cur = dummy
        while heap:
            _, i, phead = heappop(heap)
            if phead.next:
                heappush(heap, (phead.next.val, i, phead.next))
                
            cur.next = phead
            cur = cur.next
        
        return dummy.next