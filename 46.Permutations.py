class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        visited = [False] * n
        result = []
        cur = []
        self.helper(result, cur, visited, nums)
        return result

    def helper(self, result, cur, visited, nums):
        n = len(nums)
        if len(cur)==n:
            result.append(cur[:])
        for i in range(n):
            if visited[i]:
                continue
            cur.append(nums[i])
            visited[i] = True
            self.helper(result, cur, visited, nums)
            visited[i] = False
            del cur[-1]
