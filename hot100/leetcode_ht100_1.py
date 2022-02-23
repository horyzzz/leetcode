# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ten = 0
        newhead = ListNode()
        p1 = newhead
        while l1 and l2:
            val = l1.val + l2.val + ten
            if val >= 10:
                ten = 1
                val = val % 10
            else:
                ten = 0

            newhead.next = ListNode(val)
            newhead = newhead.next            
            l1 = l1.next
            l2 = l2.next

        if l1:
            go = l1
        elif l2:
            go = l2
        else:
            if ten == 1:
                newhead.next = ListNode(1)
            return p1.next

        while go:
            val = go.val + ten
            if val >= 10:
                ten = 1
                val = val % 10
            else:
                ten = 0

            newhead.next = ListNode(val)
            newhead = newhead.next            
            go = go.next

        if ten == 1:
            newhead.next = ListNode(1)

        return p1.next


l1 = ListNode()
p1 = l1
l2 = ListNode()
p2 = l2

ll1 = [2,4,3]
ll2 = [5,6,4]

for i1 in ll1:
    l1.next = ListNode(i1)
    l1 = l1.next

for i2 in ll2:
    l2.next = ListNode(i2)
    l2 = l2.next

sol = Solution()
res = sol.addTwoNumbers(p1.next, p2.next)