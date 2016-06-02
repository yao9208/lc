class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.arr = collections.deque()


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.arr)==self.size:
            self.arr.popleft()
        self.arr.append(val)
        return float(sum(self.arr))/len(self.arr)





# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
