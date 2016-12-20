from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = deque()
        visited = set()
        queue.append(beginWord)
        step = 1
        while len(queue)>0:
            step += 1
            size = len(queue)
            for k in range(size):
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for i in range(len(cur)):
                    for ch in range(ord('a'), ord('z')+1):
                        tmp = cur[:i]+chr(ch)+cur[i+1:]
                        if tmp==endWord:
                            return step
                        if tmp in wordList:
                            queue.append(tmp)
        return 0
