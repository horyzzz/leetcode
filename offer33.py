"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。

"""
class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def check(i, j):
            # j为根节点
            if i > j:
                return True
            p = i
            # 找到第一个大于根节点的节点，开始为右子树
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            # i~(m-1)为左子树
            while postorder[p] > postorder[j]:
                p += 1
            # m~(j-1)为右子树
            return p == j and check(i, m-1) and check(m, j-1)
        
        return check(0, len(postorder) - 1)