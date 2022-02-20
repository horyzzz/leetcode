# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        i = 1
        head_pre = ListNode()
        first = None
        pre, cur = None, None
        phead = head
        while head:
            if i == left - 1:
                head_pre = head
            if i == left:
                pre = None
                first = head
                cur = head
            if cur:
                next_node = cur.next
                cur.next = pre
                pre = cur
                cur = next_node
                head = next_node
            else:
                head = head.next
            
            i += 1
            if i == right + 1:
                head_pre.next = pre
                cur = None
                first.next = head
            
        if left == 1:
            return head_pre.next
        print(1)
        return phead
        

l = [1, 2, 3, 4, 5]
head = ListNode()
p1 = head
for ll in l:
    head.next = ListNode(ll)
    head = head.next

sol = Solution()
sol.reverseBetween(p1.next, 2, 4)