# Definition for singly-linked list.
"""
    给你一个单链表,随机选择链表的一个节点,并返回相应的节点值。每个节点 被选中的概率一样 。

    实现 Solution 类

    Solution(ListNode head) 使用整数数组初始化对象。
    int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random 

class Solution:

    def __init__(self, head):
        self.nodelist = []
        while head:
            self.nodelist.append(head)
            head = head.next

    def getRandom(self) -> int:
        return self.nodelist[random.randint(0, len(self.nodelist)-1)].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()