class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {}
        str = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i in range(len(str)):
            for c in str[i].lower():
                dic[c] = i
        res = []
        for word in words:
            w = word.lower()
            index = dic[w[0]]
            for c in w:
                tmp = dic[c]
                if tmp!=index:
                    tmp = -1
                    break
            if tmp!=-1:
                res.append(word)
        return res
                
