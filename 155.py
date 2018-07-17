
"""
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()

"""

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
    def pop(self):
        """
        :rtype: void
        """
        del self.stack[-1]
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1]      
    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()