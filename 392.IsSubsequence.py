class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps, pt = 0, 0
        while ps<len(s) and pt<len(t):
            if pt>=len(t) or ps>=len(s):
                return False
            elif s[ps]==t[pt]:
                ps+=1
            pt+=1
        return ps==len(s)

#follow up: preprocessing for t, + binary search
