class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        cur = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            c = s[i]
            if c in dic:
                start = max(dic[c] + 1, start)
            dic[c] = i
            longest = max(longest, i - start+1)
        return longest
