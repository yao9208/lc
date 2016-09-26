public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Comparator<int[]>(){
        public int compare(int[] arr1, int[] arr2){
            if(arr1[0] == arr2[0])
                return arr1[1] - arr2[1];
            else
                return arr1[0] - arr2[0];
       }});
       int n = people.length;
       int[][] result = new int[n][];
       List<Integer> index = new ArrayList<>();
       for (int i=0; i<n; i++){
           index.add(i);
       }
       int dup = 0;
       for (int i=0; i<n; i++){
           if(i>0 && people[i][0]==people[i-1][0]){
               dup++;
           }else{
               dup = 0;
           }
           int higher = people[i][1]-dup;
           result[index.get(higher)] = people[i];
           index.remove(higher);
       }
       return result;
    }

}
