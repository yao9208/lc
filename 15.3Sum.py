class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        p, q, r = 0,1, len(nums)-1
        while p<len(nums)-2:
            q, r = p+1, len(nums)-1
            while q<r:
                sum = nums[p]+nums[q]+nums[r]
                if sum==0:
                    result.append([nums[p],nums[q], nums[r]])
                    q+=1
                    r-=1
                    while q<r and nums[q]==nums[q-1]:
                        q+=1
                    while q<r and nums[r]==nums[r+1]:
                        r-=1
                elif sum<0:
                    q+=1
                    while q<r and nums[q]==nums[q-1]:
                        q+=1
                else:
                    r-=1
                    while q<r and nums[r]==nums[r+1]:
                        r-=1
            p+=1
            while p<len(nums)-2 and nums[p]==nums[p-1]:
                p+=1
        return result
