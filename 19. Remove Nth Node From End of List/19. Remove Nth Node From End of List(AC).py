# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        pre = length - n
        if pre == 0:
            if not head.next:
                return None
            else:
                return head.next
        else:
            cur = head
            for _ in range(pre-1):
                cur = cur.next
            if cur.next.next:
                cur.next = cur.next.next
            else:
                cur.next = None
            return head