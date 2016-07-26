class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n==0:
            return 0
        if s[0]=='0':
            return 0
        dp = [0 for x in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            if s[i-1]=='0':
                if s[i-2]=='1' or s[i-2]=='2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if (s[i-2]=='1' or s[i-2]=='2' and s[i-1]<='6') :
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[n]
