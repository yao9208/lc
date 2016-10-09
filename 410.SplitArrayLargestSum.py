class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        maxv, sumv = 0, 0
        for n in nums:
            maxv = max(maxv, n)
            sumv += n
        result = self.search(maxv, sumv, nums, m)
        return result

    def search(self, low, high, nums, m):
        while low<high:
            mid = low + (high-low)/2
            if self.valid(mid, nums, m):
                high = mid
            else:
                low = mid + 1
        return low

    def valid(self, t, nums, m):
        sum = 0
        count = 1
        for n in nums:
            sum += n
            if sum>t:
                sum = n
                count += 1
                if count>m:
                    return False
        return True
