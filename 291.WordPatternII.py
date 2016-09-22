class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        visited = set()
        return self.helper(pattern, 0, str, 0, dic, visited)

    def helper(self, p, pi, s, si, dic, visited):
        if pi==len(p) and si==len(s):
            return True
        if pi==len(p) or si==len(s):
            return False
        flag = None
        if p[pi] in dic:
            if not s[si:].startswith(dic[p[pi]]):
                return False
            else:
                length = len(dic[p[pi]])
                return self.helper(p, pi+1, s, si+length, dic, visited)
        else:
            for i in range(len(s)-si):
                sub = s[si:si+i+1]
                if sub in visited:
                    continue
                visited.add(sub)
                dic[p[pi]] = sub
                if self.helper(p, pi+1, s, si+i+1, dic, visited):
                    return True
                visited.remove(sub)
                del dic[p[pi]]
        return False
