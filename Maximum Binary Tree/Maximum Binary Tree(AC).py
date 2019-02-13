# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums,0,len(nums)-1)
        
        
    def helper(self,nums,start,end):
        if start > end :
            return None
        if start == end:
            return TreeNode(nums[start]) 
        maxIndex = nums.index(max(nums[start:end+1]))
        root = TreeNode(nums[maxIndex])
        root.left = self.helper(nums,start,maxIndex-1)
        root.right = self.helper(nums,maxIndex+1,end)
        return root