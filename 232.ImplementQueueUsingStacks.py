class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack, self.outstack = [], []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outstack.pop()


    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outstack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return (not self.instack) and (not self.outstack)

    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
