from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges)==0:
            return [0]
        dic = defaultdict(set)
        for e in edges:
            p, q = e[0], e[1]
            dic[p].add(q)
            dic[q].add(p)
        queue = deque()
        for node in dic:
            if len(dic[node])==1:
                queue.append(node)
        while n>2:
            n -= len(queue)
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for p in dic[node]:
                    dic[p].remove(node)
                    if len(dic[p])==1:
                        queue.append(p)
        return list(queue)
