class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(-1)
        k1 = 0
        k2 = 0
        dummy.next = head
        fast = head
        slow = head
        pre = dummy
        while fast:
            k1 += 1
            fast = fast.next
            if k1 > n:
                pre = slow
                slow = slow.next
        
        pre.next = slow.next
        return dummy.next