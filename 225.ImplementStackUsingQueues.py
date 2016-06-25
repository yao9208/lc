from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        newqueue = deque()
        while len(self.queue)>1:
            newqueue.append(self.queue.popleft())
        self.queue = newqueue


    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        
