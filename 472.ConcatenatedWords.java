public class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> result = new ArrayList<>();
        Arrays.sort(words, new Comparator<String>(){
            public int compare(String s1, String s2){
                return s1.length()-s2.length();
            }
        });
        Set<String> dict = new HashSet<>();
        for(int i=0; i<words.length; i++){
            if(canForm(words[i], dict)){
                result.add(words[i]);
            }
            dict.add(words[i]);
        }
        return result;
    }
    private boolean canForm(String s, Set<String> set) {
        if(set.isEmpty()){
            return false;
        }
        boolean[] dp = new boolean[s.length()+1];
        dp[0] = true;
        for(int i=1; i<=s.length(); i++){
            for(int j=0; j<i; j++){
                if(dp[j] && set.contains(s.substring(j, i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}
