class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minstack)!=0 and self.minstack[-1]>=x or len(self.minstack)==0:
            self.minstack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if len(self.minstack)!=0 and self.minstack[-1]==self.stack[-1]:
            self.minstack.pop()
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minstack)>0:
            return self.minstack[-1]
        else:
            return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
