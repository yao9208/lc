from sets import Set
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        dic = Set()
        resultSet = Set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            #key = self.transform(sub)
            if sub in dic:
                resultSet.add(sub)
            else:
                dic.add(sub)
        return list(resultSet)

    def transform(self, s):
        dic = {'A':0, 'T':1, 'C':2, 'G':3}
        result = 0
        for ch in s:
            result = result<<2+dic[ch]
        return result
