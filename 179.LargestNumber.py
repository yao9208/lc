
public class Solution {
    class NumComparator implements Comparator<Integer>{
        public int compare(Integer o1, Integer o2){
            String s1 = String.valueOf(o1);
            String s2 = String.valueOf(o2);
            String tmp1 = s1+s2;
            String tmp2 = s2+s1;
            return tmp2.compareTo(tmp1);
        }
    }
    public String largestNumber(int[] num) {
        Integer[] nums = new Integer[num.length];
        for(int i=0; i<num.length; i++){
            nums[i] = num[i];
        }
        Arrays.sort(nums, new NumComparator());
        StringBuilder b = new StringBuilder();
        for(int n:nums){
            b.append(n);
        }
        if(b.length()>0 && b.charAt(0)=='0'){
            return "0";
        }
        return b.toString();
    }
}
