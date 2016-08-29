from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dic = defaultdict(lambda:0)
        for w in words:
            dic[w] += 1
        size = len(words[0])
        m = len(words)
        result = []
        for i in range(len(s)-m*size+1):
            tmp = defaultdict(lambda:0)
            for j in range(i, i+m*size, size):
                if s[j:j+size] in dic:
                    tmp[s[j:j+size]] += 1
                else:
                    break
            if cmp(dic, tmp)==0:
                result.append(i)
        return result

#slow
