class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(1, n):
            s = self.helper(s)
        return s


    def helper(self, n):
        cur = n[0]
        count = 0
        result = ''
        for i in range(len(n)):
            if n[i]==cur:
                count+=1
            else:
                result+=str(count)+cur
                cur = n[i]
                count = 1
        result += str(count)+cur
        return result
