class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) < self.size:
            self.queue.append(val)
            sum = 0
            for i in range(len(self.queue)):
                sum += self.queue[i]
            return float(sum)/len(self.queue)
        else:
            del self.queue[0]
            self.queue.append(val)
            sum = 0
            for i in range(len(self.queue)):
                sum += self.queue[i]
            return float(sum)/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)