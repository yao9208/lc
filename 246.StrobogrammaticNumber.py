class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        num = str(num)
        start, end = 0, len(num)-1
        while start<=end:
            if num[start] in dic and num[end]==dic[num[start]]:
                start+=1
                end-=1
            else:
                return False
        if len(num)%2==1 and (num[len(num)/2]=="6" or num[len(num)/2]=="9"):
            return False
        return True
