from collections import deque, defaultdict


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        distance = {}
        result = []
        self.bfs(graph, distance, endWord, wordlist)
        self.dfs(graph, distance, endWord, wordlist, beginWord, [], result)
        return result

    def dfs(self, graph, distance, end, wordlist, cur, curlist, result):
        curlist.append(cur)
        if cur == end:
            result.append(curlist[:])
        for word in graph[cur]:
            if distance[word] == distance[cur] - 1:
                self.dfs(graph, distance, end, wordlist, word, curlist, result)
        del curlist[-1]

    def bfs(self, graph, distance, end, wordlist):
        queue = deque()
        queue.append(end)
        distance[end] = 0
        while len(queue) > 0:
            word = queue.popleft()
            for w in self.getNext(word, wordlist):
                graph[w].append(word)
                if w not in distance:
                    queue.append(w)
                    distance[w] = distance[word] + 1

    def getNext(self, word, wordlist):
        n = len(word)
        result = []
        for i in range(n):
            for ch in range(ord('a'), ord('z') + 1):
                tmp = word[:i] + chr(ch) + word[i + 1:]
                if tmp == word:
                    continue
                if tmp in wordlist:
                    result.append(tmp)
        return result
