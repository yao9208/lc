public class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int max = 0;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(!map.containsKey(c)){
                map.put(c, 1);
            }else{
                map.put(c, map.get(c)+1);
            }
            max = Math.max(max, map.get(c));
        }
        List<Character>[] freq = new List[max+1];
        for(Map.Entry<Character, Integer> entry:map.entrySet()){
            if(freq[entry.getValue()]==null){
                freq[entry.getValue()]=new ArrayList<>();
            }
            freq[entry.getValue()].add(entry.getKey());
        }
        StringBuilder b = new StringBuilder();
        for(int i=freq.length-1; i>=0; i--){
            if(freq[i]!=null){
                for(int j=0; j<freq[i].size(); j++){
                    for(int k=0; k<i; k++){
                        b.append(freq[i].get(j));
                    }
                }
            }
        }
        return b.toString();
    }
}
