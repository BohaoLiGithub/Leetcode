# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = None
        for node in lists:
            if node:
                heap.append((node.val,node))
        heapq.heapify(heap)
        while heap:
            p = heapq.heappop(heap)[1]
            #print(p.val)
            if not head:
                head = p
                cursor = p
            else:
                cursor.next = p
                cursor = cursor.next
            if p.next:
                #print("push:"+str(p.next.val))
                heapq.heappush(heap,(p.next.val,p.next))
        return head