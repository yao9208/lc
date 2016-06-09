class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        vote = 1
        for i in range(1, len(nums)):
            if nums[i]==num:
                vote += 1
            else:
                vote -= 1
                if vote==0:
                    num = nums[i]
                    vote = 1
        return num
