class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        if n==0: return result
        parent = [x for x in range(n)]
        T = [1] * n
        maxlen = 1
        last = 0
        nums.sort()
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] ==0 and T[i] < T[j]+1:
                    parent[i] = j
                    T[i] = T[j] + 1
                    if T[i] > maxlen:
                        maxlen = T[i]
                        last = i
        for i in range(maxlen):
            result.append(nums[last])
            last = parent[last]
        result.reverse()
        return result
