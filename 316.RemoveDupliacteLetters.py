class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        count = [0]*26
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        idx = 0
        for i in range(len(s)):
            if s[i]<s[idx]:
                idx = i
            if count[ord(s[i])-ord('a')]==1:
                break
            count[ord(s[i])-ord('a')] -= 1
        return s[idx] + self.removeDuplicateLetters(s[idx+1:].replace(s[idx],''))


public class Solution {
    public String removeDuplicateLetters(String s) {
        Deque<Character> stack = new LinkedList<>();
        int[] map = new int[26];
        HashSet<Character> set = new HashSet<>();
        for(int i=0; i<s.length(); i++){
            map[s.charAt(i)-'a'] ++;
        }
        for(char c:s.toCharArray()){
            int index = (int)(c-'a');
            map[index]--;
            if(set.contains(c)){
                continue;
            }
            while(!stack.isEmpty() && c<stack.peek() && map[stack.peek()-'a']!=0){
                set.remove(stack.pop());
            }
            stack.push(c);
            set.add(c);
        }
        StringBuilder b = new StringBuilder();
        while(!stack.isEmpty()){
            b.append(stack.pop());
        }
        return b.reverse().toString();
    }
}

#https://discuss.leetcode.com/topic/32259/java-solution-using-stack-with-comments
