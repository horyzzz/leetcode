# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def depth(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 1 + max(depth(root.left), depth(root.right))
        
        
        if not root:
            return True

        return abs(depth(root.left) - depth(root.right)) < 2 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
        
        