# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
                if elem:
                    curNode.left = node
                    self.queue.append(curNode.left)
            
            else:
                if elem:
                    curNode.right = node
                    self.queue.append(curNode.right)
                    self.queue.pop(0)
    
class Solution:
    def pathSum(self, root: TreeNode, target: int):
        res = []
        trace = []
        sum1 = 0

        def backtrace(trace, root, sum1):
            if not root or root.val is None:
                return 
            trace.append(root.val)
            sum1 += root.val    

            if sum1 == target and not root.left and not root.right:
                res.append(trace.copy())
                return

            if root.left:
                backtrace(trace, root.left, sum1)
                trace.pop(-1)
            if root.right:
                backtrace(trace, root.right, sum1)
                trace.pop(-1)
            
            return
        
        backtrace(trace, root, sum1)
        
        return res


A = BiTree()
LA = [0,1,1]
for x in LA:
    A.addelement(x)

sol = Solution()
target = 1
print(sol.pathSum(A.root, target))