class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s)>=2:
            for i in range(len(s)-1):
                if s[i]==s[i+1] and s[i]=='+':
                    result.append(s[:i]+'--'+s[i+2:])
        return result
        
