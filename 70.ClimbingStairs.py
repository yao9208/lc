class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        pprev, prev = 1, 2
        res = 0
        for i in range(3, n+1):
            res = pprev+prev
            pprev = prev
            prev = res
        return res
