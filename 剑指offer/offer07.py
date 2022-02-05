# Definition for a binary tree node.
"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        left_list_in = inorder[:root_index]
        left_list_pre = preorder[1:len(left_list_in)+1]
        right_list_in = inorder[root_index+1:]
        right_list_pre = preorder[len(left_list_in)+1:]
        root.left = self.buildTree(left_list_pre, left_list_in)
        root.right = self.buildTree(right_list_pre, right_list_in)
        return root