"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        stack = []
        cur = root
        pre = None
        successor = None
        while len(stack) or cur:
            #print('adsf')
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            #print(cur.val)
            if pre is not None:
                cur.left = pre
                pre.right = cur
                pre = cur
            else:
                pre = cur
                pre.left=None
                root = pre##
            temp = cur.right
            cur.right = None
            cur = temp
        a = root
        print(a.val)
        while a.right:
            a = a.right
        a.right = root
        root.left = a
        fakehead = root
        return fakehead