# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head or (head.val == val and not head.next):
            return None
        if head.val == val:
            return head.next
        
        p = head
        pre = ListNode(None)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next

        return p            
            
