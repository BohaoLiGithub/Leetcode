# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = [(0,float("inf")) for _ in range(k)]
        def inorder():
            cur = root
            stack = []
            last = float("inf")
            while cur or len(stack):
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                val = abs(cur.val - target)
                if not val > res[-1][1]:
                    for i in range(k):
                        if val < res[i][1]:
                            res.insert(i,(cur.val,val))
                            res.pop(-1)
                            break
                cur = cur.right
        inorder()
        res_ = [key for key,val in res]
        return res_