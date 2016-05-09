class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        sum = 0
        longest = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum==k:
                longest = i+1
            if (sum-k) in dic:
                longest = max(longest, i - dic[sum-k])
            if sum not in dic:
                dic[sum] = i
        return longest
