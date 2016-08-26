class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            while n>=nums[i]>0 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in xrange(n):
            if nums[i] != i+1:
                return i+1
        return n+1
                
