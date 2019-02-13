# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        p1 = None
        queue = []
        queue.insert(0,root)
        result1 = []
        result2 = []
        while queue:
            p1 = queue.pop()
            if p1:
                result1.append(p1.val)
                if p1.left:
                    queue.insert(0,p1.left)
                else:
                    queue.insert(0,None)
                if p1.right:
                    queue.insert(0,p1.right)
                else:
                    queue.insert(0,None)
            else:
                result1.append(None)
            
        queue.insert(0,root)
        while queue:
            p1 = queue.pop()
            if p1:
                result2.append(p1.val)
                queue.insert(0,p1.right if p1.right else None)
                queue.insert(0,p1.left if p1.left else None)
            else:
                result2.append(None)
        if cmp(result1,result2) == 0:
            return True
        else:
            return False
        