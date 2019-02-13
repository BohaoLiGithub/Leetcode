# inorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def minV(node):
            if not node:
                return float('-inf')
            cursor = node
            while cursor.left:
                cursor = cursor.left
            return cursor.val
        def maxV(node):
            if not node:
                return float('inf')
            cursor = node
            while cursor.right:
                cursor = cursor.right
            return cursor.val
        cursor = root
        stack = []
        #stack.insert(0,root)
        while len(stack) or cursor:
            #cursor = stack.pop(0)
            while cursor :
                stack.insert(0,cursor)
                cursor = cursor.left
            cursor = stack.pop(0)
            if cursor.left and cursor.right:
                if not (cursor.left.val <= cursor.val  <= cursor.right.val) :
                    return False
            elif cursor.left and not cursor.right :
                if not (cursor.left.val <= cursor.val):
                    return False
            elif cursor.right and not cursor.left:
                if not (cursor.val <= cursor.right.val):
                    return False
            if cursor.right and minV(cursor.right) <= cursor.val:
                return False
            if cursor.left and maxV(cursor.left) >= cursor.val:
                return False
            
            cursor = cursor.right
        return True