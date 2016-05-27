class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        prev = nums[0]
        length = len(nums)
        start, p = 1, 1
        while p<len(nums):
            if nums[p]!=prev:
                nums[start]=nums[p]
                start+=1
                prev = nums[p]
            else:
                length-=1
            p+=1
        return length
