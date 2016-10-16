from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result, maxCount = 0, 0
        start, end = 0, 0
        dic = defaultdict(lambda:0)
        while end<len(s):
            dic[s[end]] += 1
            maxCount = max(maxCount, dic[s[end]])
            while end-start+1-maxCount>k:
                dic[s[start]]-=1
                start+=1
                maxCount = max(dic.values())
            result = max(result, end-start+1)
            end+=1
        return result
