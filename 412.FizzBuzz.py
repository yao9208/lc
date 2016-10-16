class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            cur = ''
            if i%3==0:
                cur = "Fizz"
            if i%5==0:
                cur += "Buzz"
            if i%3!=0 and i%5!=0:
                cur = str(i)
            result.append(cur)
        return result
