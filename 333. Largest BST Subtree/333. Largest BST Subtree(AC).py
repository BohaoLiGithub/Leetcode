# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Subtree(object):
    def __init__(self,largest,maxvalue,minvalue,num):
        self.largest = largest
        self.maxvalue = maxvalue
        self.minvalue = minvalue
        self.num = num
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        bst = self.isBST(root)
        return bst.largest
    
    def isBST(self,root):
        if not root:
            return Subtree(0,float('-inf'),float('inf'),0)
        left = self.isBST(root.left)
        right = self.isBST(root.right)
        if root.val > left.maxvalue and root.val < right.minvalue:
            print ('if:')
            print("root: "+ str(root.val))
            print ("left: "+ str(left.num))
            print ("right: "+ str(right.num))
            n = left.num + right.num + 1
        else:
            n = float('-inf')
        largest = max(left.largest, right.largest, n)
        return Subtree(largest,max(right.maxvalue,root.val),min(left.minvalue,root.val),n)