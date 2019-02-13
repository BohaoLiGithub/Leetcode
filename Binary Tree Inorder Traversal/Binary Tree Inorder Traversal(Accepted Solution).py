class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root
        if root == None:
            return []
        #stack.insert(0,root)
        while len(stack) or cur != None:
            while cur != None:
                stack.insert(0,cur)
                cur = cur.left
            cur = stack.pop(0)
            res.append(cur.val)
            cur = cur.right
        return res