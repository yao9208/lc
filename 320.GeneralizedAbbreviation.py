class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = set()
        if len(word)==0:
            return [""]
        word = list(word)
        result.add(''.join(word))
        for i in range(1, len(word)+1):
            for j in range(len(word)-i+1):
                tmp = word[0:j]+[str(i)]+word[j+i:]
                if j+i+1<len(word):
                    post = self.generateAbbreviations(word[j+i+1:])
                    for p in post:
                        result.add(''.join(word[0:j]+[str(i)]+[word[j+i]]+[p]))
                result.add(''.join(tmp))
        return list(result)

public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> result = new ArrayList<>();
        helper(result, word, "", 0, 0);
        return result;
    }
    private void helper(List<String> result, String word, String cur, int pos, int count){
        if(pos==word.length()){
            if(count>0){
                cur+=count;
            }
            result.add(cur);
            return;
        }
        helper(result, word, cur, pos+1, count+1);
        helper(result, word, cur+(count>0? count:"")+word.charAt(pos), pos+1, 0);
    }
}
