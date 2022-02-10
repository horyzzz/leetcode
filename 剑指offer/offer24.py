"""
    剑指 Offer 24. 反转链表
    定义一个函数,输入一个链表的头节点,反转该链表并输出反转后链表的头节点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
class Solution:
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

