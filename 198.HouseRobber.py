class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pprev, prev, result = 0, 0, 0
        for n in nums:
            result = max(pprev+n, prev)
            pprev = prev
            prev = result
        return result
