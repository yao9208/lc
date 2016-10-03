from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = defaultdict(lambda:0)
        for ch in s:
            dic[ch] += 1
        result = 0
        flag = False
        for key in dic:
            if dic[key]%2==1:
                if not flag:
                    result += dic[key]
                    flag = True
                else:
                    result += dic[key]-1
            else:
                result += dic[key]
        return result
        
