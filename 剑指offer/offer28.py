# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def Symmetric(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return Symmetric(L.left, R.right) and Symmetric(L.right, R.left)
        
        return Symmetric(root.left, root.right)
