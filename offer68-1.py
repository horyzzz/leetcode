# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father = root
        while True:
            if father.val > p.val and father.val > q.val:
                father = father.left
            elif father.val < p.val and father.val < q.val:
                father = father.right
            else:
                break
        return father