class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        n = len(heights)
        result = 0
        for i in range(n+1):
            cur = 0 if i==n else heights[i]
            while len(stack)!=0 and cur<=heights[stack[-1]]:
                t = stack.pop()
                w = i if len(stack)==0 else i-stack[-1]-1
                result = max(result, w*heights[t])
            stack.append(i)
        return result
