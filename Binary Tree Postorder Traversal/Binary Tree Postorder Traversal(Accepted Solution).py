# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = []
        cur = root
        last = root
        stack.insert(0,root)
        while stack:
            cur = stack[0]
            if (cur.left == None and cur.right == None) or (cur.left == last and cur.right == None) or (cur.right == last):
                stack.pop(0)
                res.append(cur.val)
                last = cur
            else:
                if cur.right:
                    stack.insert(0,cur.right)
                if cur.left:
                    stack.insert(0,cur.left)
        
        return res