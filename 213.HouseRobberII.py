class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]  #corner case
        return max(self.helper(nums, 0, n-2), self.helper(nums, 1, n-1))

    def helper(self, nums, start, end):
        pprev, prev, result = 0, 0, 0
        for i in range(start, end+1):
            cur = max(pprev+nums[i], prev)
            pprev = prev
            prev = cur
            result = max(result, cur)
        return result
