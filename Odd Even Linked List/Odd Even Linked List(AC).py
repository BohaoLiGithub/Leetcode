# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        oddhead = ListNode(0)
        evenhead = ListNode(0)
        cursor = head
        dummy1_cur = oddhead
        dummy2_cur = evenhead
        while cursor:
            dummy1_cur.next = cursor
            dummy1_cur = dummy1_cur.next
            cursor = cursor.next
            dummy2_cur.next = cursor
            dummy2_cur = dummy2_cur.next
            if cursor:
                cursor = cursor.next
        if evenhead.next:
            dummy1_cur.next = evenhead.next
        else:
            dummy1_cur.next = None
        return oddhead.next