public class Solution {
    class Item{
        int n, idx, rank;
        public Item(int n, int idx){
            this.n = n;
            this.idx = idx;
        }
    }
    public String[] findRelativeRanks(int[] nums) {
        Item[] a = new Item[nums.length];
        for(int i=0; i<nums.length; i++){
            a[i] = new Item(nums[i], i);
        }
        Arrays.sort(a, (x, y)-> y.n-x.n);
        for(int i=0; i<nums.length; i++){
            a[i].rank = i+1;
        }
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "Gold Medal");
        map.put(2, "Silver Medal");
        map.put(3, "Bronze Medal");
        Arrays.sort(a, (x, y)->x.idx-y.idx);
        String[] res = new String[nums.length];
        for(int i=0; i<nums.length; i++){
            if(a[i].rank<=3){
                res[i] = map.get(a[i].rank);
            }else{
                res[i] = String.valueOf(a[i].rank);
            }
        }
        return res;
    }
}
