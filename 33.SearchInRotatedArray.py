class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start, end = 0, n-1
        while start < end:
            mid = start + (end-start)/2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[start]:
                if nums[start]<=target and target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid]<target and target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        if nums[start]==target:
            return start
        return -1

#https://discuss.leetcode.com/topic/3538/concise-o-log-n-binary-search-solution
