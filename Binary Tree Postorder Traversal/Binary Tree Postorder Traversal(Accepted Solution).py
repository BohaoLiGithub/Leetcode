# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# There are three different situations which allow us pop a node from the stack
# (1) This node doesnt have both left and right child
# (2) This node doesn't have right child and the last node being popped from stack is the left child of this node
# (3) The last node popped from the stack is the right child of this node
# We use an extra pointer to record the last node popped from the stack

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