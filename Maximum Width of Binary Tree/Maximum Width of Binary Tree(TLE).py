# 104 / 108

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        depth = self.getDepth(root)
        if depth == 0:
            return 0
        nodeList = [[] for i in range(depth)]
        #print (depth)
        nodeList = self.helper(0,depth-1,root,nodeList)
        maxWid = 1
        for i in range(len(nodeList)-1,0,-1):
            firstIndex = 0
            lastIndex = len(nodeList[i]) -1
            while firstIndex < lastIndex:
                flag1 = False
                flag2 = False
                if not nodeList[i][firstIndex] == 'null':
                    flag1 = True
                else:
                    firstIndex += 1
                if not nodeList[i][lastIndex] == 'null':
                    flag2 = True
                else:
                    lastIndex -= 1
                if flag1 and flag2:
                    break;
            temp = lastIndex - firstIndex + 1
            if temp > 2**(i-1):
                maxWid = max(maxWid,temp)
                return maxWid
            else:
                maxWid = max(maxWid,temp)
        return maxWid
        
    def getDepth(self,root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left),self.getDepth(root.right))
    def helper(self,level,depth,root,nodeList):
        #print (depth)
        #print (level)
        if level > depth:
            return None
        if not root:
            nodeList[level].append('null')
            root = TreeNode('null')
        else:
            #print ("in else " + str(level))
            nodeList[level].append(root.val)
        self.helper(level+1,depth,root.left,nodeList)
        self.helper(level+1,depth,root.right,nodeList)
        return nodeList