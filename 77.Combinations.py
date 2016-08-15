class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n==k or k==0:
            return [[(i+1) for i in range(k)]]
        left = self.combine(n-1, k-1)
        for l in left:
            l.append(n)
        right = self.combine(n-1, k)
        return left + right

#normal search like combination sum?
