class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start, result = 0, 0
        for i in range(len(s)):
            c = s[i]
            if c in dic:
                start = max(start, dic[c]+1)
            dic[c] = i
            result = max(result, i-start+1)
        return result
