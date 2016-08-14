class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        n = len(digits)
        if n==0:
            return []
        cur = ['']
        for i in range(n):
            c = digits[i]
            for s in cur:
                for ch in dic[c]:
                    result.append(s+ch)
            cur = result
            result = []
        return cur
