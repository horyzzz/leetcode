# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        if not head:
            return None
        
        p1, p2 = head, head
        for _  in range(k):
            if not p1:
                return head
            p1 = p1.next
        
        pre, cur, nxt = None, p2, p2
        while cur != p1:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        p2.next = self.reverseKGroup(p1, k)
        
        return pre
        
        
        