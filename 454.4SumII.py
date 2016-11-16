from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict = defaultdict(lambda:0)
        result = 0
        for c in C:
            for d in D:
                dict[c+d] += 1
        for a in A:
            for b in B:
                result += dict[0-a-b] if (0-a-b) in dict else 0
        return result
