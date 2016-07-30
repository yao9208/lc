class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        start, end = 0, n-1
        res = [0 for x in range(n)]
        if a>=0:
            index = n-1
        else:
            index = 0
        while start <= end:
            nstart = self.transform(nums[start], a, b, c)
            nend = self.transform(nums[end], a, b ,c)
            if a >=0:
                if nstart >= nend:
                    res[index] = nstart
                    index -= 1
                    start+=1
                else:
                    res[index] = nend
                    index -= 1
                    end-=1
            else:
                if nstart <= nend:
                    res[index] = nstart
                    index+=1
                    start+=1
                else:
                    res[index] = nend
                    index +=1
                    end -=1
        return res


    def transform(self, num, a, b, c):
        return a * num * num + b * num + c
