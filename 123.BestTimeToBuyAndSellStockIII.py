class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1:
            return 0
        left, right = [0]*n, [0]*n
        minv = prices[0]
        profit = 0
        for i in range(1, n):
            profit = max(profit, prices[i] - minv)
            left[i] = profit
            minv = min(minv, prices[i])
        maxv = prices[n-1]
        profit = 0
        for i in range(n-2, -1, -1):
            profit = max(maxv-prices[i], profit)
            right[i] = profit
            maxv = max(maxv, prices[i])
        result = 0
        for i in range(n):
            result = max(result, left[i]+right[i])
        return result
