class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0: return 0
        if n==1: return k
        same, diff = k, k*(k-1)
        for i in range(2, n):
            same, diff = diff, (same+diff)*(k-1)
        return same+diff
