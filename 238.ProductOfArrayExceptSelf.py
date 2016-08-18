class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result
