class TrieNode(object):
    def __init__(self):
        self.nodes = [None]*26
        self.flag = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.nodes[ord(ch)-ord('a')]:
                node.nodes[ord(ch)-ord('a')] = TrieNode()
            node = node.nodes[ord(ch)-ord('a')]
        node.flag = True

    def search(self, word):
        node = self.root
        for ch in word:
            if not node.nodes[ord(ch)-ord('a')]:
                return False
            node = node.nodes[ord(ch)-ord('a')]
        if not node.flag:
            return False
        return True

    def startWith(self, word):
        node = self.root
        for ch in word:
            if not node.nodes[ord(ch)-ord('a')]:
                return False
            node = node.nodes[ord(ch)-ord('a')]
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        visited = [[False]*n for x in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(result, board, i, j, '', trie, visited)
        return list(result)

    def dfs(self, result, board, x, y, prefix, trie, visited):
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return
        if visited[x][y]:
            return
        prefix += board[x][y]
        if not trie.startWith(prefix):
            return
        if trie.search(prefix):
            result.add(prefix)
        visited[x][y] = True
        self.dfs(result, board, x+1, y, prefix, trie, visited)
        self.dfs(result, board, x-1, y, prefix, trie, visited)
        self.dfs(result, board, x, y+1, prefix, trie, visited)
        self.dfs(result, board, x, y-1, prefix, trie, visited)
        visited[x][y] = False
        
