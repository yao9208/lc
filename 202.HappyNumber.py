from sets import Set
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = Set()
        while True:
            dic.add(n)
            tmp = self.cal(n)
            if tmp == 1:
                return True
            else:
                if tmp in dic:
                    return False
            n = tmp
        return False

    def cal(self, n):
        result = 0
        while n>0:
            result += (n%10)**2
            n /= 10
        return result
