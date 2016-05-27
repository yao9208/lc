class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, p = 0, 0
        while p<len(nums):
            if nums[p]!=0:
                nums[start] = nums[p]
                start+=1
            p+=1
        while start<len(nums):
            nums[start]=0
            start+=1
