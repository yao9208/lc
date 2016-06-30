class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = sys.maxint
        maxpro = 0
        for price in prices:
            minprice = min(minprice, price)
            maxpro = max(maxpro, price-minprice)
        return maxpro
