class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        mid = start + (end-start)/2
        while start <= end:
            prev, next = -sys.maxint-1, -sys.maxint-1
            if mid>0:
                prev = nums[mid-1]
            if mid<len(nums)-1:
                next = nums[mid+1]
            if nums[mid]>prev and nums[mid]>next:
                return mid
            elif nums[mid]<prev:
                end = mid-1
            else:
                start = mid+1
            mid = start + (end-start)/2
        return mid
