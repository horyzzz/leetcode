# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode1(self, head):
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        
        t = 0
        while head and t < l // 2:
            t += 1
            head = head.next
        return head
    
    def middleNode(self, head):
        """
            双指针
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
