class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        if len(words[0])!=n:
            return False
        for i in range(n):
            string = words[i]
            tmp = ''
            for j in range(n):
                if len(words[j])>i:
                    tmp += words[j][i]
            if string!=tmp:
                return False
        return True
