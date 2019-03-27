# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        linkedlistarray = []
        if head is None or not head.next:
            return None
        fast = head
        slow = head
        while True:
            if not fast or not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cur = slow # meeting point
                break
        slow = head
        fast = cur
        index = 0
        while slow != fast:
            index += 1
            slow = slow.next
            fast = fast.next
        return slow