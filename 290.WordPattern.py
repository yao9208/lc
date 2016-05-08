class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False
        return len(set(pattern)) == len(set(strs)) == len(set(zip(pattern, strs)))

#or use 2 dicts
