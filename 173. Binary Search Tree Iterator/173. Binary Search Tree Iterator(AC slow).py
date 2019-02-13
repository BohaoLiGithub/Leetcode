# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.BST = []
        def inOrder(root,list_):
            if not root:
                return
            inOrder(root.left,list_)
            list_.append(root.val)
            inOrder(root.right,list_)
        inOrder(root,self.BST)
        self.size = len(self.BST)
        def it():
            for val in self.BST:
                self.size -= 1
                yield val
        self.it = it()
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return next(self.it)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.size != 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()