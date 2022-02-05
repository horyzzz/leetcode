# Definition for a binary tree node.
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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def comp(A, B):
            if not B:
                return True
            elif not A or A.val != B.val:
                return False
            return comp(A.left, B.left) and comp(A.right, B.right)
        
        return (A and B) and (comp(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

sol = Solution()
A = BiTree()
B = BiTree()
LA = [1, 2, 3, 4]
for x in LA:
    A.addelement(x)
LB = [3]
for x in LB:
    B.addelement(x)

print(sol.isSubStructure(A.root, B.root))