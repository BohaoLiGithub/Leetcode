# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cursor = head
        pro_cursor = None
        pre_cursor = None
        while cursor:
            val = cursor.val
            if cursor.next:
                pro_cursor = cursor.next
                while pro_cursor:
                    if pro_cursor.val == val:
                        pro_cursor = pro_cursor.next  
                    else:
                        break;
            else:
                break
            if cursor.next != pro_cursor:
                if pre_cursor:
                    pre_cursor.next = pro_cursor
                elif not pro_cursor and pre_cursor:
                    pre_cursor.next = None
                    break;
                else:
                    head = pro_cursor
                    pre_cursor = None
            else:
                pre_cursor = cursor
            cursor = pro_cursor
        return head