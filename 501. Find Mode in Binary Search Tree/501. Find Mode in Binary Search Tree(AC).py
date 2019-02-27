# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = collections.deque()
        #dict_ = collections.defaultdict(list)
        counter = collections.Counter()
        queue.appendleft(root)
        while len(queue):
            cur = queue.pop()
            counter[cur.val] += 1
            if cur.left:
                queue.appendleft(cur.left)
            if cur.right:
                queue.appendleft(cur.right)
        max_ = max(counter.values())
        return [p for p in counter if counter[p] == max_]