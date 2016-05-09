class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashset = set()
        for ch in s:
            if ch in hashset:
                hashset.remove(ch)
            else:
                hashset.add(ch)
        return len(hashset)<=1
