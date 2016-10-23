class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dic = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.dic:
            self.dic[number]=True
        else:
            self.dic[number] = False


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.dic:
            if value-key in self.dic:
                if key*2==value and self.dic[key]==True:
                    return True
                elif key*2!=value:
                    return True
                else:
                    continue
        return False
#https://discuss.leetcode.com/topic/32449/trade-off-in-this-problem-should-be-considered


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
