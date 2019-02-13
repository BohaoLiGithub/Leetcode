# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        list1 = []
        self.inOrder(root,list1)
        if len(list1) == 1:
            return list1[0]
        start,end = 0, len(list1)-1
        while start <= end:
            mid = (start + end)/2
            if list1[mid] == target:
                return list1[mid]
            elif list1[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        index = end if end >= 0 else 0
        if index == len(list1) - 1:
            print('in if')
            return list1[-1]
        else:
            return list1[index] if target - list1[index] < list1[index+1] - target else list1[index + 1]
    def inOrder(self,root,li):
        if not root:
            return
        self.inOrder(root.left,li)
        li.append(root.val)
        self.inOrder(root.right,li)