# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        cursor1 = p
        cursor2 = q
        queue1 = list()
        queue2 = list()
        queue1.insert(0,p)
        queue2.insert(0,q)
        while len(queue1) and len(queue2):
            cursor1 = queue1.pop(0)
            cursor2 = queue2.pop(0)
            if not cursor1.val == cursor2.val:
                return False
            if (cursor1.left and not cursor2.left) or ( not cursor1.left and cursor2.left):
                return False
            elif cursor1.left and cursor2.left:
                queue1.insert(0,cursor1.left)
                queue2.insert(0,cursor2.left)
            if (cursor1.right and not cursor2.right) or ( not cursor1.right and cursor2.right):
                return False
            elif cursor1.right and cursor2.right:
                queue1.insert(0,cursor1.right)
                queue2.insert(0,cursor2.right)
        if len(queue1) or (queue2):
            return False
        else:
            return True