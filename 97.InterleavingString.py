class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m+n!=len(s3):
            return False
        if m==n==0:
            return s3==''
        dp = [[False]*(n+1) for x in range(m+1)]
        flag = True
        for i in range(m):
            if s1[i]!=s3[i]:
                flag = False
            dp[i+1][0] = flag
        flag = True
        for i in range(n):
            if s2[i]!=s3[i]:
                flag = False
            dp[0][i+1] = flag
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] and s3[i+j-1]==s1[i-1] or dp[i][j-1] and s3[i+j-1]==s2[j-1]
        return dp[m][n]
