class Solution(object):
    dic = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.dic:
            return self.dic[s]
        s = list(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1]=='+':
                s[i]=s[i+1]='-'
                string = ''.join(s)
                flag = self.canWin(string)
                self.dic[string] = flag
                s[i]=s[i+1]='+'
                if not flag:
                    return True
        self.dic[''.join(s)] = False
        return False
