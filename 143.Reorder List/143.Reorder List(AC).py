# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        mid = self.findMid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2_new = self.reverse(l2)
        c1,c2 = l1,l2_new
        dummyhead = ListNode(0)
        cur = dummyhead
        while c1 and c2:
            backup1 = c1.next
            backup2 = c2.next
            cur.next = c1
            cur = cur.next
            cur.next = c2
            cur = cur.next
            c1 = backup1
            c2 = backup2
        if c1:
            cur.next = c1
            cur = cur.next
        cur.next = None
        return dummyhead.next
        
    def findMid(self,head):
        if not head:
            return None
        if not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self,head):
        if not head:
            return None
        if not head.next:
            return head
        a,b = head,head.next
        while b:
            c = b.next
            b.next = a
            if a == head:
                a.next = None
            a = b
            b = c
        return a