class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1, set2 = set(), set()
        for c in s:
            if c in set1:
                set2.add(c)
            set1.add(c)
        for i in range(len(s)):
            if s[i] not in set2:
                return i
        return -1
