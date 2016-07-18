class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 1, num
        while start <= end:
            mid = start + (end - start) / 2
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
