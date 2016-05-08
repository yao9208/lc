class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic1 and t[i] not in dic2:
                dic1[s[i]] = t[i]
                dic2[t[i]] = s[i]
            elif s[i] not in dic1 or t[i] not in dic2:
                return False
            elif dic1[s[i]]==t[i] and dic2[t[i]] == s[i]:
                    continue
            else:
                return False
        return True
