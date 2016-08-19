class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for k in range(2, len(nums)):
            i, j = 0, k-1
            while i<j:
                if nums[i]+nums[j]+nums[k]<target:
                    count += j-i
                    i += 1
                else:
                    j -= 1
        return count
                    
