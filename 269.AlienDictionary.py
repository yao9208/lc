from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(set)
        for i in range(1, len(words)):
            for j in range(min(len(words[i-1]), len(words[i]))):
                if words[i-1][j]!=words[i][j]:
                    graph[words[i-1][j]].add(words[i][j])
                    break
        indegree = {}
        for word in words:
            for ch in word:
                if ch not in indegree:
                    indegree[ch] = 0
        for key in graph:
            for word in graph[key]:
                indegree[word]+=1
        queue = deque()
        for key in indegree:
            if indegree[key]==0:
                queue.append(key)
        result = ''
        while len(queue)>0:
            cur = queue.popleft()
            result += cur
            if cur in graph:
                for key in graph[cur]:
                    indegree[key]-=1
                    if indegree[key]==0:
                        queue.append(key)
        if len(result)!=len(indegree):
            return ''
        return result
