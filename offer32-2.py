"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""

import collections

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BiTree(object):
    def __init__(self):
        self.root = None
        self.queue = []
    
    def addelement(self, elem):
        node = TreeNode(elem)
        if not self.root:
            self.root = node
            self.queue.append(self.root)

        else:
            curNode = self.queue[0]
            if not curNode.left:
                curNode.left = node
                self.queue.append(curNode.left)
            
            else:
                curNode.right = node
                self.queue.append(curNode.right)
                self.queue.pop(0)

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        res, queue = [], collections.deque()
        queue.append(root)

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
            res.append(tmp)
        
        return res


q = [3,9,20,None,None,15,7]
Tree = BiTree()
for qq in q:
    Tree.addelement(qq)

sol = Solution()
print(sol.levelOrder(Tree.root))


    