class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = [0]*26
        for c in s:
            dic[ord(c)-ord('a')] += 1
        for c in t:
            dic[ord(c)-ord('a')] -= 1
        for i in range(len(dic)):
            if dic[i]!=0:
                return chr(i+ord('a'))
        return None
