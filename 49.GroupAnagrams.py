class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        result = []
        for key in dic:
            result.append(sorted(dic[key]))
        return result
