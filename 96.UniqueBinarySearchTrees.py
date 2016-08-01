class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]
