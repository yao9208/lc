class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        s = list(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]=='+':
                s[i]=s[i+1]='-'
                result.append(''.join(s))
                s[i]=s[i+1]='+'
        return result
