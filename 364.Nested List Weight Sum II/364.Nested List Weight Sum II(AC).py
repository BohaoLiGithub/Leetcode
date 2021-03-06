# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        #print(type(nestedList))
        total_depth = self.getDepth(nestedList,1)
        return self.cal(nestedList,0,total_depth)
        
    def cal(self,nestedList,depth,total_depth):
        res = 0
        for val in nestedList:
            if val.isInteger():
                res += val.getInteger() * (total_depth-depth)
            else:
                res += self.cal(val.getList(),depth+1,total_depth)
        return res
            
        
    def getDepth(self,nestedList,depth):
        max_depth = depth
        for var in nestedList:
            if not var.isInteger():
                max_depth = max(self.getDepth(var.getList(),depth+1),max_depth)
        return max_depth