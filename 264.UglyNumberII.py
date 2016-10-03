class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]*n
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            tmp = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            if tmp == ugly[p2]*2:
                p2 += 1
            if tmp == ugly[p3]*3:
                p3 += 1
            if tmp == ugly[p5]*5:
                p5 += 1
            ugly[i] = tmp
        return ugly[n-1]
