class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        queue = []
        dic = {}
        if not node:
            return None
        queue.append(node)
        start = 0
        while start < len(queue):
            cur = queue[start]
            neighbors = cur.neighbors
            if cur not in dic:
                dic[cur] = UndirectedGraphNode(cur.label)
                for item in neighbors:
                    queue.append(item)
            start+=1
        for item in dic:
            neighbors = item.neighbors
            for neighbor in neighbors:
                dic[item].neighbors.append(dic[neighbor])
        return dic[node]
