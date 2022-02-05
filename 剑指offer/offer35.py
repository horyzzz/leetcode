# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
        哈希表,字典
    """
    def copyRandomList1(self, head: 'Node') -> 'Node':
        if not head:
            return None

        cur = head
        Nodedict = {}
        while cur:
            Nodedict[cur] = Node(cur.val)
            cur = cur.next

        newhead = head
        while newhead:
            Nodedict[newhead].next = Nodedict.get(newhead.next)
            Nodedict[newhead].random = Nodedict.get(newhead.random)
            newhead = newhead.next

        return Nodedict[head]

    """
        辅助连表 
        https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/jian-zhi-offer-35-fu-za-lian-biao-de-fu-zhi-ha-xi-/
    """
    def copyRandomList1(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        # 复制节点,并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 构建新节点的random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分两个链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res
        



