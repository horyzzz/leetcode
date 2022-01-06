"""
    剑指 Offer 06. 从尾到头打印链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head):
        instack = []
        while head:
            instack.append(head.val)
            head = head.next

        outstack = []
        while instack:
            outstack.append(instack.pop())

        return outstack
