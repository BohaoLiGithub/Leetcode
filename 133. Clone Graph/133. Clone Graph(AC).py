"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        queue = collections.deque([])
        queue.append(node)
        mirror = {Node:Node}
        newNode = Node(node.val,[])
        mirror[node] = newNode
        while queue:
            node_ = queue.popleft() #ori
            for nei in node_.neighbors:
                if nei not in mirror:
                    newNei = Node(nei.val,[])
                    mirror[nei] = newNei
                    mirror[node_].neighbors.append(newNei)
                    queue.append(nei)
                else:
                    mirror[node_].neighbors.append(mirror[nei])
        return newNode