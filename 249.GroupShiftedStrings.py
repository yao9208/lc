class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for string in strings:
            key = self.hashfunc(string)
            if key in result:
                result[key].append(string)
            else:
                result[key] = [string]
        for key in result:
            result[key].sort()
        return result.values()

    def hashfunc(self, s):
        shift = ord(s[0]) - ord('a')
        key = ""
        for ch in s:
            hashed = ord(ch)-shift
            if hashed < ord('a'):
                hashed += 26
            key = key+chr(hashed)
        return key
