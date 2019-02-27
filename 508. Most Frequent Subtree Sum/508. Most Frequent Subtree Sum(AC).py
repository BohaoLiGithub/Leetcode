# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        def getSum(node):
            if not node:
                return 0
            val = node.val + getSum(node.left) + getSum(node.right)
            counter[val] += 1
            return val
        counter = collections.Counter()
        getSum(root)
        freq = max(counter.values())
        return [s for s in counter if counter[s] == freq]