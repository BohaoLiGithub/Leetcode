# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return []
        head1, head2 = None , None
        cursor = head
        cur1 ,cur2 = None,None
        while cursor != None:
            value = cursor.val
            node = ListNode(value)
            if value < x : 
                if head1 == None:
                    head1 = node
                    cur1 = head1
                    
                else:
                    cur1.next = node
                    cur1 = cur1.next
            else:
                if head2 == None:
                    head2 = node
                    cur2 = head2
                else:
                    cur2.next = node
                    cur2 = cur2.next
            cursor = cursor.next
        if isinstance(cur1,ListNode):
            cur1.next = head2
            return head1
        else:
            return head2