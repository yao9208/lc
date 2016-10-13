public class Solution {
    public List<String> readBinaryWatch(int num) {
      List<String> result = new ArrayList<>();
        int[] nums1 = new int[]{1,2,4,8}, nums2 = new int[]{1,2,4,8,16,32};
        for(int i=0; i<=num; i++){
          List<Integer> hour = generateDigit(nums1, i);
          List<Integer> min = generateDigit(nums2, num-i);
          for(int h:hour){
            if(h>=12) continue;
            for(int m:min){
              if(m>=60) continue;
              String tmp = h+":"+(m<10?("0"+m):m);
              result.add(tmp);
            }
          }
        }
        return result;
    }
    private List<Integer> generateDigit(int[] nums, int count){
      List<Integer> result = new ArrayList<>();
      helper(result, nums, count, 0, 0);
      return result;
    }
    private void helper(List<Integer> res, int[] nums, int count, int cur, int start){
      if(count==0){
        res.add(cur);
        return;
      }
      for(int i=start; i<nums.length; i++){
        helper(res, nums, count-1, cur+nums[i], i+1);
      }
    }
}
