class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A,B,m,n = B,A,n,m
        imin, imax, half = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imin+imax)/2
            j = half - i
            if j>0 and i<m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i==0: maxleft = B[j-1]
                elif j==0: maxleft = A[i-1]
                else: maxleft = max(A[i-1], B[j-1])
                if (m+n)%2==1:
                    return maxleft
                if i==m: minright = B[j]
                elif j==n: minright = A[i]
                else: minright = min(A[i], B[j])
                return (maxleft+minright)/2.0
