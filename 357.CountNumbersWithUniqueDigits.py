class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        result = 10
        choice = 9
        cur = 9
        while n>1:
            choice = choice * cur
            result += choice
            cur -= 1
            n -= 1
        return result


#another solution is backtracking https://discuss.leetcode.com/topic/48001/backtracking-solution/2
