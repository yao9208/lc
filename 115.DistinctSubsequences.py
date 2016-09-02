class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t), len(s)
        dp = [[0]*(n+1) for x in range(m+1)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if t[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]
        
