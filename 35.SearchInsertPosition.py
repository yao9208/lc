class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end-start)/2
            if nums[mid]<target:
                start = mid + 1
            else:
                end = mid
        if nums[start]<target:
            return start+1
        return start
