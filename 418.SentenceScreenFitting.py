class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        length = [0]*n
        for i in range(n):
            j = i
            cur = 0
            curlen = 0
            while (curlen+len(sentence[j]))<=cols:
                cur += 1
                curlen += len(sentence[j])+1
                j = (j+1)%n
            length[i] = cur
        start = 0
        total = 0
        for i in range(rows):
            total += length[start]
            start = total % n
        return total/n
