class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        m, n = len(word), len(abbr)
        i , j = 0, 0
        tmp =0
        while i<n:
            if abbr[i]>='0' and abbr[i]<='9':
                if abbr[i]=='0':
                    return False
                while i<n and abbr[i]>='0' and abbr[i]<='9':
                    tmp = tmp*10 + int(abbr[i])
                    i += 1
                j += tmp
                tmp =0
            else:
                if j>=m or abbr[i]!=word[j]:
                    return False
                i += 1
                j += 1
        return i==n and j==m

            
