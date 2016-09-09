class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min1, min2 = -1, -1
        if len(costs)==0:
            return 0
        n, k = len(costs), len(costs[0])
        for i in range(n):
            for j in range(k):
                if j==min1:
                    costs[i][j] += costs[i-1][min2] if i>0 else 0
                else:
                    costs[i][j] += costs[i-1][min1] if i>0 else 0
            cost1, cost2 = sys.maxint, sys.maxint
            for j in range(k):
                if costs[i][j]<cost1:
                    min2, cost2 = min1, cost1
                    cost1 = costs[i][j]
                    min1 = j
                elif costs[i][j]<cost2:
                    cost2 = costs[i][j]
                    min2 = j
        return costs[n-1][min1]
