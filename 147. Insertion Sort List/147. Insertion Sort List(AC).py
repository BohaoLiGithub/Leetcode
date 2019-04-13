# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        cur = head.next
        head.next = None
        newHead = head
        while cur:
            backup = cur.next
            val = cur.val     
            cur_in = newHead
            pre = None
            insertion = False
            while cur_in:
                if val <= cur_in.val:
                    if pre:
                        pre.next = cur
                        cur.next = cur_in
                    else:
                        cur.next = newHead
                        newHead = cur
                    insertion = True
                    break
                pre = cur_in
                cur_in = cur_in.next
            if not insertion:
                pre.next = cur
                cur.next = None
            cur = backup
        return newHead