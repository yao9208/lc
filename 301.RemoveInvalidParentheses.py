from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = set()
        queue = deque()
        queue.append(s)
        visited.add(s)
        res = []
        found = False
        while len(queue)!=0:
            cur = queue.popleft()
            if self.isValid(cur):
                res.append(cur)
                found = True
            if found:
                continue
            for i in range(len(cur)):
                if cur[i]!='(' and cur[i]!=')':
                    continue
                tmp = cur[0:i]+cur[i+1:]
                if tmp not in visited:
                    visited.add(tmp)
                    queue.append(tmp)
        return res

    def isValid(self, s):
        count = 0
        for c in s:
            if c!='(' and c!=')':
                continue
            if c=='(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    return False
        return count == 0
