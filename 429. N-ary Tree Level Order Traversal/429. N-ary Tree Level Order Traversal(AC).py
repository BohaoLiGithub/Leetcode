"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return[]
        res = []
        queue = collections.deque()
        level = 1
        queue.append((root,level))
        while len(queue):
            temp,last_level = queue.popleft()
            #print(str(temp.val)+': '+str(last_level))
            if len(res) < last_level:
                res.append([temp.val])
                level += 1
            else:
                res[last_level-1].append(temp.val)
            for i in range(len(temp.children)):
                queue.append((temp.children[i],level))
        return res