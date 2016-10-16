class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = 1
        for i in range(2, n):
            factorial *= i
        cur = n-1
        nums = [i+1 for i in range(n)]
        result = []
        k-=1
        while len(nums)>1:
            idx = k/factorial
            result.append(str(nums[idx]))
            nums.remove(nums[idx])
            k %= factorial
            factorial /= cur
            cur-=1
        result.append(str(nums[0]))
        return ''.join(result)
