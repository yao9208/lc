public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if(s==null || s.length()<=3){
            return result;
        }
        int n = s.length();
        for(int i=1; i<=Math.min(3, n-3); i++){
            if(n-i>9 || i>1 && s.charAt(0)=='0'){
                continue;
            }
            for(int j=i+1; j<=i+3 && j<=n-2; j++){
                if(n-j>6 || j>i+1 && s.charAt(i)=='0'){
                    continue;
                }
                for(int k=j+1; k<=j+3 && k<=n-1; k++){
                    if(n-k>3 || k>j+1 && s.charAt(j)=='0'){
                        continue;
                    }
                    if(n-k>1 && s.charAt(k)=='0'){
                        continue;
                    }
                    int num1 = Integer.parseInt(s.substring(0, i));
                    int num2 = Integer.parseInt(s.substring(i, j));
                    int num3 = Integer.parseInt(s.substring(j, k));
                    int num4 = Integer.parseInt(s.substring(k));
                    if (num1<=255 && num2<=255 && num3<=255 && num4<=255){
                        String str = s.substring(0, i)+"."+s.substring(i, j)+"."+s.substring(j, k)+"."+s.substring(k);
                        result.add(str);
                    }
                }
            }
        }
        return result;
    }
}
