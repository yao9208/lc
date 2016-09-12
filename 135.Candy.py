class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        a = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                a[i] = a[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                a[i] = max(a[i+1]+1, a[i])
        return sum(a)
