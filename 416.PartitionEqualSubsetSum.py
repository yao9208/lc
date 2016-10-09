class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2==1:
            return False
        volumn = s/2
        dp = [False]*(volumn+1)
        dp[0] = True
        for i in range(1, len(nums)+1):
            for j in range(volumn, nums[i-1]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i-1]]
        return dp[volumn]
