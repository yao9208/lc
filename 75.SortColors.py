class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 2
            if tmp == 1:
                nums[q]=1
                q+=1
            if tmp == 0:
                nums[q]=1
                nums[p]=0
                p+=1
                q+=1
