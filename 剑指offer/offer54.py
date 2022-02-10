# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
            BST 中序遍历为有序遍历,左根右（顺序） 右根左（逆序）
        """

        if not root or k == 0:
            return
        self.i = 0

        def midorder(root):
            if not root:
                return       

            midorder(root.right)
            
            self.i += 1
            if self.i == k:
                self.res = root.val
            
            midorder(root.left)

        midorder(root)
        return self.res