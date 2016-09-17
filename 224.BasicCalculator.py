class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numstack = []
        signstack = []
        num = 0
        result = 0
        sign = 1
        i= 0
        while i < len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+=1
                result += sign*num
                num = 0
            if i>=len(s):
                break
            if s[i]=='+':
                sign = 1
            elif s[i]=='-':
                sign = -1
            elif s[i]=='(':
                numstack.append(result)
                signstack.append(sign)
                result = 0
                sign = 1
            elif s[i]==')':
                result = numstack.pop() + signstack.pop() * result
            i += 1
        return result
        
