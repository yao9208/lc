class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return []
        n = len(s)
        matrix = [[False]*(n) for x in range(n)]
        for i in range(n):
            matrix[i][i] = True
        for i in range(n-1):
            matrix[i][i+1] = s[i]==s[i+1]
        for k in range(2, n):
            for i in range(n-k):
                matrix[i][i+k] = matrix[i+1][i+k-1] and s[i]==s[i+k]

        dp = [i-1 for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if matrix[j][i-1]==True:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[n]
