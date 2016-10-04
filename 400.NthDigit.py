class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        length = 1
        count = 9
        while n> length*count:
            n -= length*count
            count *= 10
            length += 1
            start *= 10
        start += (n-1)/length
        return int(str(start)[(n-1)%length])

        
