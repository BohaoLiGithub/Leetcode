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
        stack1 = []
        stack2 = []
        stack1.append(p)
        stack2.append(q)
        last1, last2 = None, None
        pos1, pos2 = None, None
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            if pos1!= pos2:
                return False
            if node1.right:
                stack1.append(node1.right)
                pos1 = 'right'
            if node2.right:
                stack2.append(node2.right)
                pos2 = 'right'
            if node1.left:
                stack1.append(node1.left)
                pos1 = 'left'
            if node2.left:
                stack2.append(node2.left)
                pos2 = 'left'
        if stack1 or stack2:
            #print('1')
            return False
        else:
            return True
            
        