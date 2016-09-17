class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        count = [0]*26
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        idx = 0
        for i in range(len(s)):
            if s[i]<s[idx]:
                idx = i
            if count[ord(s[i])-ord('a')]==1:
                break
            count[ord(s[i])-ord('a')] -= 1
        return s[idx] + self.removeDuplicateLetters(s[idx+1:].replace(s[idx],''))
