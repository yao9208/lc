class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        maxv, minv = nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp = max(maxv*nums[i], minv*nums[i], nums[i])
            minv = min(maxv*nums[i], minv*nums[i], nums[i])
            maxv = tmp
            result = max(result, maxv)
        return result
