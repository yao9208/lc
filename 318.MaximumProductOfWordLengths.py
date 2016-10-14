class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        mask = [0]*n
        for i in range(n):
            for ch in words[i]:
                mask[i] |= 1<<(ord(ch)-ord('a'))
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                if mask[i]&mask[j]==0:
                    result = max(result, len(words[i])*len(words[j]))
        return result
