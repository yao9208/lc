from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic = defaultdict(lambda:0)
        for c in p:
            dic[c]+=1
        count = len(p)
        start, end = 0, 0
        result = []
        while end<len(s):
            if end>=len(p):
                if s[start] in dic:
                    dic[s[start]]+=1
                    if dic[s[start]]>0:
                        count+=1
                start+=1
            if s[end] in dic:
                dic[s[end]]-=1
                if dic[s[end]]>=0:
                    count-=1
                    if count==0:
                        result.append(start)
            end+=1
        return result
