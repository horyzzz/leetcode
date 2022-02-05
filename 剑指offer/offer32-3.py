import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        res, queue = [], collections.deque()
        queue.append(root)
        n = 0
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val != None:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            n += 1
            if n % 2 == 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
        return res
