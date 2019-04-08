# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(inorder,preorder):
            if inorder:
                head_val = preorder.pop(0)
                head = TreeNode(head_val)
                idx = inorder.index(head_val)
                head.right = helper(inorder[idx+1:],preorder)
                head.left = helper(inorder[:idx],preorder)
                return head
        right_pre_order = postorder[::-1]
        head = helper(inorder,right_pre_order)
        return head
        