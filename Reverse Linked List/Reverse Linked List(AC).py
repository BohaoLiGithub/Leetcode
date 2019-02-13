# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cursor = head
        if not head.next:
            return head
        pre_cur = head.next
        while pre_cur:
            if cursor == head:
                cursor.next = None
            temp = pre_cur.next
            pre_cur.next = cursor
            cursor = pre_cur
            pre_cur = temp 
        head= cursor
        return head