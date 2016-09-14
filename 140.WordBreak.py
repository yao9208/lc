class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dic = {}
        return self.helper(s, wordDict, dic)


    def helper(self, s, wordDict, dic):
        if s in dic:
            return dic[s]
        result = []
        if len(s)==0:
            return ['']
        for word in wordDict:
            if s.startswith(word):
                post = self.helper(s[len(word):], wordDict, dic)
                for item in post:
                    result.append(word+('' if len(item)==0 else ' ')+item)
        dic[s] = result
        return result
