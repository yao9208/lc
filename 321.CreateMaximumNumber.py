class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        res = []
        for i in range(max(0,k-n), min(k, m)+1):
            a = self.maxArray(nums1, i)
            b = self.maxArray(nums2, k-i)
            tmp = self.merge(a, b, k)
            if self.greater(tmp,0, res,0):
                res = tmp
        return res

    def merge(self, a, b, k):
        res = []
        i, j = 0, 0
        for p in range(k):
            if self.greater(a, i, b, j):
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        return res

    def greater(self, a, i, b, j):
        m, n = len(a), len(b)
        while i<m and j<n and a[i]==b[j]:
            i+=1
            j+=1
        return j==len(b) or i<m and a[i]>b[j]

    def maxArray(self, nums, k):
        n = len(nums)
        p = 0
        res = []
        for i in range(n):
            while p > 0 and n - i - 1 >= k - p and nums[i] > res[-1]:
                res.pop()
                p-=1
            if p<k:
                res.append(nums[i])
                p += 1
        return res
