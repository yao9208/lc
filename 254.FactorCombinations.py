import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result, cur = [], []
        self.helper(2, n, result, cur)
        return result

    def helper(self, start, n, result, cur):
        if n==1:
            if len(cur)>1:
                result.append(cur[:])
            return
        for i in range(start, int(math.sqrt(n))+1):
            if (n%i)==0:
                cur.append(i)
                self.helper(i, n/i, result, cur)
                del cur[-1]
        cur.append(n)
        self.helper(n, 1, result, cur)
        del cur[-1]
