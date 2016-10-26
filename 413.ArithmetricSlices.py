class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n<=2:
            return 0
        dp = [0]*n
        result = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                result += dp[i]
        return result


#slice! not subsequence!
