class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        result = 0
        diff = sys.maxint
        for i in range(n-2):
            j, k = i+1, n-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                dif = abs(sum-target)
                if dif<diff:
                    diff = dif
                    result = sum
                if sum<target:
                    j+=1
                else:
                    k-=1
        return result
