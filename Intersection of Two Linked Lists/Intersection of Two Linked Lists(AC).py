# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        len1, len2 = 0, 0
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        p1 = headA
        p2 = headB
        
        if len1 > len2:
            for _ in range(len1 - len2):
                p1 = p1.next
        elif len1 < len2:
            for _ in range(len2 - len1):
                p2 = p2.next
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
            