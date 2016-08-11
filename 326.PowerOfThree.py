from math import log
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxPower = 3 ** int(log(0x7fffffff)/log(3))
        return n > 0 and maxPower%n==0


from math import log10
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (log10(n)/log10(3))%1==0
