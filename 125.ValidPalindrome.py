class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start, end = 0, len(s)-1
        while start < end:
            while start<end and s[start].isalnum()==False:
                start += 1
            while start<end and s[end].isalnum()==False:
                end -= 1
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
