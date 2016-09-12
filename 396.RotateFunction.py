import sys
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)==0:
            return 0
        n = len(A)
        num = sum(A)
        cur = sum([i*A[i] for i in range(n)])
        result = cur
        for i in range(1, n):
            cur = cur+num-n*A[n-i]
            result = max(result, cur)
        return result
        
