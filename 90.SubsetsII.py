class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        last = 0
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                start = last
            else:
                start = 0
            last = len(result)
            n=len(result)
            for j in range(start, n):
                tmp = result[j]+[nums[i]]
                result.append(tmp)
        return result


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, cur = [], []
        nums.sort()
        self.helper(result, cur, 0, nums)
        return result

    def helper(self, result, cur, start, nums):
        result.append(cur[:])
        for i in range(start, len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            cur.append(nums[i])
            self.helper(result, cur, i+1, nums)
            del cur[-1]
