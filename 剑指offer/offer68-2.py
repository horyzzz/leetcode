# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
            递归
            三种情况：
            1、p,q分别在root左右，返回root
            2、p(q)为root，q(p)为左子树节点
            3、p(q)为root，q(p)为右子树节点
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return root