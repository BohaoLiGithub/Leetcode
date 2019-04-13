"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur = head
        dummyhead = Node(0,None,None)
        cur_n = dummyhead
        dict_ = collections.defaultdict()
        while cur:
            val = cur.val
            next_ = cur.next
            ran = cur.random
            n = Node(val,next_,None)
            dict_[cur] = n
            cur_n.next = n
            cur_n = cur_n.next
            cur = cur.next
        cur_n = dummyhead.next
        cur = head
        while cur:
            if cur.random:
                cur_n.random = dict_[cur.random]
            cur_n = cur_n.next
            cur = cur.next
        return dummyhead.next