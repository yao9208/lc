from collections import deque
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = deque()
        if len(tokens)==0:
            return 0
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.evaluate(a, b, t))
            else:
                stack.append(int(t))
        return stack[-1]

    def evaluate(self, a, b, t):
        if t=="+":
            return a+b
        elif t=="-":
            return a-b
        elif t=="*":
            return a*b
        else:
            return int(float(a)/b)
