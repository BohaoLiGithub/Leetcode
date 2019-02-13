# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cursor1 = node
        cursor2 = node.next
        while True:
            cursor1.val = cursor2.val
            if not cursor2.next:
                cursor1.next = None
                break
            cursor2 = cursor2.next
            cursor1 = cursor1.next
        