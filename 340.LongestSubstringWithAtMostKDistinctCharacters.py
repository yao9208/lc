from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, end = 0, 0
        dic = defaultdict(lambda:0)
        result = 0
        while end < len(s):
            dic[s[end]] += 1
            while len(dic)>k:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    del dic[s[start]]
                start += 1
            result = max(result, end-start+1)
            end += 1
        return result
