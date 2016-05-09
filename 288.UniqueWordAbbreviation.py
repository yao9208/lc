class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = collections.defaultdict(set)
        for s in dictionary:
            key = s
            if len(s)>2:
                key = s[0] + str(len(s)-2) + s[-1]
            self.dic[key].add(s)


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = word
        if len(key)>2:
            key = word[0] + str(len(word)-2) + word[-1]
        return len(self.dic[key])==0 or len(self.dic[key])==1 and list(self.dic[key])[0]==word



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
