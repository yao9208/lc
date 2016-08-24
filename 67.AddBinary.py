class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        result = ''
        carry = 0
        for i in range(n):
            na = 0 if len(a)-1-i<0 else int(a[-i-1])
            nb = 0 if len(b)-1-i<0 else int(b[-i-1])
            cur = (na+nb+carry)%2
            carry = (na+nb+carry)>>1
            result += str(cur)
        if carry == 1:
            result+='1'
        return result[::-1]
