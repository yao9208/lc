from collections import defaultdict
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic = [0]*26
        if len(s1)!=len(s2):
            return False
        for ch in s1:
            dic[ord(ch)-ord('a')]+=1
        for ch in s2:
            dic[ord(ch)-ord('a')]-=1
        for n in dic:
            if n!=0:
                return False
        if len(s1)<=1:
            return True
        for i in range(1, len(s1)):
            success = self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[0:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[0:len(s1)-i])
            if success:
                return True
        return False
