class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        cur = []
        self.search(result, s, 0, cur)
        return result

    def search(self, result, s, start, cur):
        if start==len(s):
            result.append(cur[:])
        for end in range(start, len(s)):
            if self.isValid(s, start, end):
                cur.append(s[start:end+1])
                self.search(result, s, end+1, cur)
                del cur[-1]


    def isValid(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
