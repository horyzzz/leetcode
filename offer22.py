# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
            第一个指针先走k步，第二个指针开始走
            当第一个指针走到最后，第二个指针刚好走到倒数第k个（n-k）
        """
        p1 = p2 = head
        step = 0
        while p1:
            step += 1
            if step > k:
                p2 = p2.next
            p1 = p1.next
        
        return p2
            
