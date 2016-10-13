public class Solution {
    public int lastRemaining(int n) {
        int head = 1, step = 1, remaining = n;
        boolean left = true;
        while(remaining>1){
          if(left || remaining%2==1){
            head = head+step;
          }
          step*=2;
          left=!left;
          remaining/=2;
        }
        return head;
    }
}
