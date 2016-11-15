class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid]==target:
                return True
            if nums[mid]>nums[start]:
                if nums[start]<=target and target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            elif nums[mid]<nums[start]:
                if nums[mid]<target and target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                start+=1
        return False

#make stronger boarder restriction than q33
