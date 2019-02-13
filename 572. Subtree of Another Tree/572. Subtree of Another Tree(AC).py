# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        cursor = None
        result = False
        queue = []
        queue.insert(0,s)
        while queue:
            cursor = queue.pop()
            if cursor.val == t.val:
                result = self.isPart(cursor,t)
                if result:
                    return True
            if cursor.left:
                queue.insert(0,cursor.left)
            if cursor.right:
                queue.insert(0,cursor.right)
        return False
    
    def isPart(self,n1,n2):
        if not n1 and not n2:
            return True
        if (not n1 and n2) or (not n2 and n1):
            return False
        if n1.val != n2.val:
            return False
        return self.isPart(n1.left,n2.left) and self.isPart(n1.right,n2.right)