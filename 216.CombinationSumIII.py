class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result, cur = [], []
        self.search(result, cur, 1, k, n)
        return result

    def search(self, result, cur, start, k, n):
        if len(cur)>k or n<0:
            return
        if len(cur)==k and n==0:
            result.append(cur[:])
            return
        for i in range(start, 10):
            cur.append(i)
            self.search(result, cur, i+1, k, n-i)
            del cur[-1]
