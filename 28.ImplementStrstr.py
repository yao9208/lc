class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            j = 0
            while j<n and needle[j]==haystack[i+j]:
                j+=1
            if j==n:
                return i
        return -1

            
