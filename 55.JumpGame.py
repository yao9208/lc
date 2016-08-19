class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = 0
        for i in range(len(nums)):
            result = max(result, i+nums[i])
            if result>=len(nums)-1:
                return True
            if result==i:
                return False
        return False
