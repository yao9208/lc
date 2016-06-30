from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = deque()
        dirs = path.split('/')
        for dir in dirs:
            if len(dir)!=0:
                if dir=="..":
                    if len(stack)!=0:
                        stack.pop()
                elif dir!=".":
                    stack.append(dir)
        return self.makestr(stack)

    def makestr(self, stack):
        result = ""
        if not stack or len(stack)==0:
            return "/"
        for dir in stack:
            result += "/"+dir
        return result
