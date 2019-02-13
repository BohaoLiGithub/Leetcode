class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        max_value = self.maxstack[-1] if len(self.maxstack) > 0 else None
        if max_value is None or x > max_value:
            max_value = x
        self.stack.append(x)
        self.maxstack.append(max_value)
        #print("push:")
        #print (self.stack)

    def pop(self):
        """
        :rtype: int
        """
        self.maxstack.pop() if len(self.maxstack) > 0 else None
        return self.stack.pop() if len(self.stack) > 0 else None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if len(self.stack) > 0 else None

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxstack[-1] if len(self.maxstack) > 0 else None

    def popMax(self):
        """
        :rtype: int
        """
        #print("pop max")
        max_value = self.peekMax()
        if max_value is not None:
            #print (max_value)
            tempstack = []
            while self.top() != max_value:
                #print (self.maxstack)
                #print (self.stack)
                self.maxstack.pop()
                temp = self.stack.pop()
                tempstack.append(temp)
            self.stack.pop()
            self.maxstack.pop()
            while len(tempstack) != 0:
                temp = tempstack.pop(-1)
                self.push(temp)
        return max_value
        

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()