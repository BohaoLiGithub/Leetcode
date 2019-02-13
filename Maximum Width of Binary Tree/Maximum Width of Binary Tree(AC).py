# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object)
    def widthOfBinaryTree(self, root)
        
        type root TreeNode
        rtype int
        
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue
            if node
                queue.append((node.left, depth+1, pos2))
                queue.append((node.right, depth+1, pos2 + 1))
                if cur_depth != depth
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans