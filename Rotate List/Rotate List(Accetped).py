# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cursor = head
        length = 1
        while cursor.next:
            cursor = cursor.next
            length += 1
        cursor.next = head
        cursor1 = head
        a = length - k % length
        #newhead = head
        i = 0
        while i != a-1 :
            cursor1 = cursor1.next
            i += 1
        newhead = cursor1.next
        cursor1.next = None
        return newhead