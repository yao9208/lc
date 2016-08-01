class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1] * (target+1)
        dp[0] = 1
        return self.helper(nums, target, dp)

    def helper(self, nums, target, dp):
        if dp[target]!=-1:
            return dp[target]
        result = 0
        for n in nums:
            if target >= n:
                result += self.helper(nums, target-n, dp)
        dp[target] = result
        return result

#https://discuss.leetcode.com/topic/52302/1ms-java-dp-solution-with-detailed-explanation
