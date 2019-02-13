class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        def it():
            for line in vec2d:
                for val in line:
                    self.size -= 1
                    yield val   
										
        self.it = it()
        self.size = sum(len(line) for line in vec2d)

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
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())