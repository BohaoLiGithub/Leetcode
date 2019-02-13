# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        pre, target, pos = self.findNode(root,key)
        if not target:
            return root
        if not target.left and not target.right: # leaf
            #print('if')
            if not pre:
                return None
            else:
                if pos == 'left':
                    pre.left = None
                else:
                    pre.right = None
                return root
        elif (target.left and not target.right) or (target.right and not target.left): #has only one subtree
            #print('elif')
            if not pre:
                return target.left if target.left else target.right
            else:
                if pos == 'left':
                    pre.left = target.left if target.left else target.right
                else:
                    pre.right = target.left if target.left else target.right
                return root
        else: # has two subtrees
            #print('else')
            pre_minRight, minRight = self.minValueofRightSubtree(target)
            #print (target.val)
            target.val = minRight.val
            if pre_minRight:
                pre_minRight.left = self.deleteNode(minRight,minRight.val)
            else:
                target.right = self.deleteNode(minRight,minRight.val)
            return root
                
    def findNode(self,root,key):
        cursor = root
        pre_cur = None
        pos = None
        while cursor:
            if cursor.val == key:
                return pre_cur, cursor, pos
            elif key < cursor.val:
                pre_cur = cursor
                pos = 'left'
                cursor = cursor.left
            else:
                pre_cur = cursor
                pos = 'right'
                cursor = cursor.right
        return None,None,None
    def minValueofRightSubtree(self,target): ## the min value of the right subtree
        cursor = target.right
        pre = None
        while cursor.left:
            pre = cursor
            cursor = cursor.left
        return pre, cursor
        