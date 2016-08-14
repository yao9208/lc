class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result, cur = [], []
        candidates.sort()
        self.search(candidates, result, cur, 0, target)
        return result

    def search(self, candidates, result, cur, start, target):
        n = len(candidates)
        if target<0:
            return
        if target==0:
            result.append(cur[:])
        for i in range(start, n):
            cur.append(candidates[i])
            self.search(candidates, result, cur, i, target-candidates[i])
            del cur[-1]
