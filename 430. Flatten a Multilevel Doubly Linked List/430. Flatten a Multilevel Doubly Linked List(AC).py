"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur = head
        while cur:
            if cur.child:
                next_ = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                lastChild = self.DFS(cur.child) # end of the child linked list
                cur.child = None
                lastChild.next = next_
                if next_:
                    next_.prev = lastChild
            cur = cur.next
        return head
                
        
    def DFS(self,node):
        cur = node
        while cur.next:
            if cur.child:
                next_ = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                lastChild = self.DFS(cur.child) # end of the child linked list
                cur.child = None
                lastChild.next = next_
                if next_:
                    next_.prev = lastChild
            cur = cur.next
        return cur