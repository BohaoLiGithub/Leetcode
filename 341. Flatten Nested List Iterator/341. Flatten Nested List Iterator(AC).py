# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def it(nlist):
            for el in nlist:
                if el.isInteger():
                    self.size -= 1
                    #print(el.getInteger())
                    yield el.getInteger()
                else: #list
                    #print('else')
                    for e in it(el.getList()):
                        yield e
        self.it = it(nestedList)
        def size_(nlist):
            size = 0
            for el in nlist:
                if el.isInteger():
                    size += 1
                else:
                    size += size_(el.getList())
            return size
        self.size = size_(nestedList)
    def next(self):
        """
        :rtype: int
        """
        return next(self.it)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.size != 0 else False
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())