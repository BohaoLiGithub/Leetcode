# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return True
        p1 = head
        if not head.next:
            return True
        p2 = head.next
        p3 = p2.next
        
        forward = []
        while p1:
            forward.append(p1.val)
            p1 = p1.next
    
        p1 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            if p1 == head:
                p1.next = None
            p1 = p2
            p2 = p3
        reverse = []
        while p1:
            reverse.append(p1.val)
            p1 = p1.next
        if cmp(forward,reverse) == 0:
            return True
        else:
            return False