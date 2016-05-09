class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        sum, longest = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum-k) in dic:
                longest = max(longest, i - dic[sum-k])
            if sum not in dic:
                dic[sum] = i
        return longest
