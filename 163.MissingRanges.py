class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        for i in range(len(nums)+1):
            prev = lower-1 if i==0 else nums[i-1]
            cur = upper+1 if i==len(nums) else nums[i]
            if cur!=prev+1:
                result.append(self.helper(prev+1, cur-1))
        return result

    def helper(self, low, high):
        if low==high:
            return str(low)
        return str(low)+'->'+str(high)
