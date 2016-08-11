class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dic = [0]*26
        for c in magazine:
            mag_dic[ord(c)-ord('a')] += 1
        for c in ransomNote:
            if mag_dic[ord(c)-ord('a')]<1:
                return False
            mag_dic[ord(c)-ord('a')] -= 1
        return True
