class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        sum = 0
        maxlen = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                maxlen = i+1
            elif sum-k in dic:
                maxlen = max(maxlen, i-dic[sum-k])
            if sum not in dic:
                dic[sum] = i
        return maxlen
