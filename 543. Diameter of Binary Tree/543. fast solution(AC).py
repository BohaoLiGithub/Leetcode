# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object)
    def diameterOfBinaryTree(self, root)
        
        type root TreeNode
        rtype int
        
        self.result = 0
        
        def depth(root)
            if not root
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.result = max(self.result,left+right)
            return 1 + max(left,right)
        depth(root)
        return self.result