#Definition for a binary tree node.
"""
    从上到下打印出二叉树的每个节点,同一层的节点按照从左到右的顺序打印。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = [root.val]
        while queue:
            root = queue.pop(0)
            if root.left:
                queue.append(root.left)
                res.append(root.left.val)
            if root.right:
                queue.append(root.right)
                res.append(root.right.val)
        return res

