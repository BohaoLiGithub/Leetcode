# There are two different situations: the target node has right child or not
# If the node has the right child. what we need to do is to find the minimum node in its right subtree
# If the node doesnt have, we have to recursively find its ancestor until one node is the left child of its parent
# If we find this kind of node, we just need return this node;
# If we can't find that, that means the target node is the very right of the entire tree, return None

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        if node.right: # node has the right child
            cur_ = node.right
            while cur_.left:
                cur_ = cur_.left
            return cur_
        else: # node has not the right child
            parent = node.parent
            son = node
            if not parent:
                return None
            while son == parent.right:
                son = parent
                parent = parent.parent
                if not parent:
                    return None
            return parent