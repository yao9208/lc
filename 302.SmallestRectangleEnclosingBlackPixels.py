class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        left = self.searchCol(image, 0, y, True)
        right = self.searchCol(image, y + 1, n, False)
        top = self.searchRow(image, 0, x, True)
        bottom = self.searchRow(image, x + 1, m, False)
        return (right - left) * (bottom - top)

    def searchCol(self, image, x, y, opt):
        # left
        start, end = x, y
        m = len(image)
        while start < end:
            mid = start + (end - start) / 2
            i = 0
            while i < m and image[i][mid] == '0':
                i += 1
            if (i < m) == opt:
                end = mid
            else:
                start = mid + 1
        return start

    def searchRow(self, image, x, y, opt):
        start, end = x, y
        n = len(image[0])
        while start < end:
            mid = start + (end - start) / 2
            i = 0
            while i < n and image[mid][i] == '0':
                i += 1
            if (i < n) == opt:
                end = mid
            else:
                start = mid + 1
        return start
        
