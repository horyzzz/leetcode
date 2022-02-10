class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        p1 = headA
        p2 = headB
        """
        解决这个问题的关键是,通过某些方式,让 p1 和 p2 能够同时到达相交节点 c1。

        所以,我们可以让 p1 遍历完链表 A 之后开始遍历链表 B,让 p2 遍历完链表 B 之后开始遍历链表 A,这样相当于「逻辑上」两条链表接在了一起。

        如果这样进行拼接,就可以让 p1 和 p2 同时进入公共部分,也就是同时到达相交节点 c1:


        """
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1