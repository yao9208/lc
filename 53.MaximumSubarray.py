class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur, result = 0, -sys.maxint
        for n in nums:
            if cur <= 0:
                cur = n
            else:
                cur += n
            result = max(result, cur)
        return result
