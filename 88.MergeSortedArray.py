class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q = m-1, n-1
        ptr = m+n-1
        while q>=0:
            if p<0 or nums1[p]<=nums2[q]:
                nums1[ptr]=nums2[q]
                q-=1
            else:
                nums1[ptr]=nums1[p]
                p-=1
            ptr-=1
