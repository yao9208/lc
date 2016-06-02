class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                elif dic[stack[-1]]!=ch:
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        return False
