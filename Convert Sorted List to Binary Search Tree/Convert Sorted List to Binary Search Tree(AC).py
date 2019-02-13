# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        nodesList = list()
        p = head
        while p:
            nodesList.append(p.val)
            p = p.next
        
        def helper(start,end):
            if start > end:
                return None
            index = int((start + end)//2)
            node = TreeNode(nodesList[index])
            node.left = helper(start,index - 1)
            node.right = helper(index+1,end)
            return node
        
        return helper(0,len(nodesList) - 1)
        