class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<=end:
            mid = (start+end)/2
            prev = -sys.maxint if mid==0 else nums[mid-1]
            next = -sys.maxint if mid==len(nums)-1 else nums[mid+1]
            if nums[mid]>prev and nums[mid]>next:
                return mid
            elif nums[mid]<prev:
                end = mid-1
            else:
                start = mid+1
        return -1
