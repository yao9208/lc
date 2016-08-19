class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k, l = j+1, n-1
                while k<l:
                    num = nums[i]+nums[j]+nums[k]+nums[l]
                    if num==target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        k+=1
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        l-=1
                    elif num<target:
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        k+=1
                    else:
                        while k<l and nums[l]==nums[l-1]:
                            l-=1
                        l-=1
        return result

#TLE
