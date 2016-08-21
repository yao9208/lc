class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = [0]*256
        count = 0
        for ch in t:
            dic[ord(ch)] += 1
            count += 1
        start, end = 0, 0
        minlen = sys.maxint
        index = None
        for end in range(len(s)):
            dic[ord(s[end])] -= 1
            if dic[ord(s[end])]>=0:
                count-=1
                while count==0:
                    cur = end-start+1
                    if cur<minlen:
                        minlen = cur
                        index = start
                    dic[ord(s[start])]+=1
                    if dic[ord(s[start])]>0:
                        count+=1
                    start+=1
        if index is None:
            return ''
        return s[index:index+minlen]
        
