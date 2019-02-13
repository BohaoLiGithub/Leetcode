# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        self.inorder(root,nodes)
        for i in range(len(nodes)):
            if p == nodes[i]:
                return nodes[i+1] if int(i) != len(nodes) - 1 else None
    def inorder(self,root,nodes):
        if not root:
            return
        self.inorder(root.left,nodes)
        nodes.append(root)
        self.inorder(root.right,nodes)
            