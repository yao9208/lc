class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        visited = [False] * n
        result = []
        cur = []
        nums.sort()
        self.helper(result, cur, visited, nums)
        return list(result)

    def helper(self, result, cur, visited, nums):
        n = len(nums)
        if len(cur)==n:
            result.append(cur[:])
        for i in range(n):
            if visited[i] or (i>0 and not visited[i-1] and nums[i]==nums[i-1]):
                continue
            cur.append(nums[i])
            visited[i] = True
            self.helper(result, cur, visited, nums)
            visited[i] = False
            del cur[-1]
