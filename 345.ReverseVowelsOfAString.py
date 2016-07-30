class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = set('aeiouAEIOU')
        start, end = 0, len(s)-1
        ls = list(s)
        while start<end:
            if ls[start] not in dic:
                start += 1
            elif ls[end] not in dic:
                end -= 1
            else:
                ls[start], ls[end] = ls[end], ls[start]
                start += 1
                end -= 1
        return ''.join(ls)
