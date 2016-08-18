class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(result, '', n, 0)
        return result

    def helper(self, result, s, n, m):
        if n==0 and m==0:
            result.append(s)
        if n>0:
            self.helper(result, s+'(', n-1, m+1)
        if m>0:
            self.helper(result, s+')', n, m-1)
