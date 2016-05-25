class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums)-1
        result = [-1,-1]
        while start < end:
            mid = start + (end - start)/2 + 1
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        if nums[end]!=target:
            return result
        last = end
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end - start)/2
            if nums[mid] <target:
                start = mid+1
            else:
                end = mid
        if nums[start]!=target:
            return result
        first = start
        return [first, last]
