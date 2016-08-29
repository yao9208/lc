class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                prefix = word[0:j]
                post = word[j:]
                if self.isPalindrome(prefix):
                    if post[::-1] in dic and dic[post[::-1]]!=i:
                        result.append([dic[post[::-1]], i])
                if self.isPalindrome(post) and len(post)>0:
                    if prefix[::-1] in dic and dic[prefix[::-1]]!=i:
                        result.append([i, dic[prefix[::-1]]])
        return result

    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start]!=s[end]:
                return False
            start += 1
            end -= 1
        return True
