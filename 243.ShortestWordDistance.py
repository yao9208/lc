class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p, q = -1, -1
        result = sys.maxint
        for i in range(len(words)):
            if words[i]==word1:
                p = i
            elif words[i]==word2:
                q = i
            if p!=-1 and q!=-1:
                result = min(result, abs(p-q))
        return result
        
