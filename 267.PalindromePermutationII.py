from collections import defaultdict
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = self.isValid(s)
        if dic is None:
            return []
        mid = None
        half = ''
        for key in dic:
            half += key*(dic[key]//2)
            if dic[key]%2==1:
                mid = key
        prefix = self.permute(half)
        result = []
        for pre in prefix:
            if mid:
                result.append(pre+mid+pre[::-1])
            else:
                result.append(pre+pre[::-1])
        return result

    def permute(self, s):
        result = []
        cur = []
        self.helper(result, cur, s, [False]*len(s))
        return result

    def helper(self, result, cur, s, visited):
        if len(cur)==len(s):
            result.append(''.join(cur[:]))
            return
        for i in range(len(s)):
            if visited[i] or (i>0 and not visited[i-1] and s[i-1]==s[i]):
                continue
            cur.append(s[i])
            visited[i]=True
            self.helper(result, cur, s, visited)
            del cur[-1]
            visited[i]=False

    def isValid(self, s):
        dic = defaultdict(lambda: 0)
        for ch in s:
            dic[ch] += 1
        odd = 0
        for key in dic:
            if dic[key]%2==1:
                odd += 1
            if odd>1:
                return None
        return dic
