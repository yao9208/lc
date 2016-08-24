class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for z in zip(*strs):
            bag = set(z)
            if len(bag)==1:
                prefix += bag.pop()
            else:
                break
        return prefix
