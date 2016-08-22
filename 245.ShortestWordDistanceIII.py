class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minlen = sys.maxint
        p, q = -1, -1
        for i in range(len(words)):
            if words[i]==word1:
                if words[i]==word2 and p!=-1:
                    minlen = min(minlen, i-p)
                p = i
            elif words[i]==word2:
                q = i
            if p!=-1 and q!=-1:
                minlen = min(minlen, abs(q-p))
        return minlen
