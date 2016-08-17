class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        before = self.grayCode(n-1)
        flag = 1<<(n-1)
        size = len(before)
        for i in range(size-1, -1, -1):
            before.append(flag + before[i])
        return before

#iterative?
