class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        low, high = nums[0], nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]+1:
                result.append(self.generate(low, high))
                low, high = nums[i], nums[i]
            else:
                high = nums[i]
        result.append(self.generate(low, high))
        return result
    def generate(self, start, end):
        if start==end:
            return str(start)
        return str(start)+'->'+str(end)
