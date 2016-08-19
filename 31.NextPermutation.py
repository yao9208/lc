class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i==-1:
            self.reverse(nums, 0, n-1)
            return
        self.reverse(nums, i+1, n-1)
        for j in range(i+1, n):
            if nums[j]>nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                return

    def reverse(self, s, start, end):
        while start<end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
