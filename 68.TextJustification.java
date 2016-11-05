public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int n = words.length;
        int i=0;
        while(i<n){
            int start = i;
            StringBuilder b = new StringBuilder();
            int len = 0, count = 0;
            int space = 0;
            while(i<n && len+words[i].length()+1<=maxWidth){
                len += words[i].length()+1;
                count ++;
                i++;
            }
            if(i==n){
                space = count-1;
            }
            else if(i<n && len+words[i].length()<=maxWidth){
                len += words[i].length();
                count++;
                i++;
                space = count-1;
            }else{
                space = maxWidth-len+count;
            }

            int remain = count==1? 0:space%(count-1), gap = count==1? space: space/(count-1);
            for(int j=0; j<count; j++){
                b.append(words[start+j]);
                if(remain>0){
                    b.append(' ');
                    remain--;
                }
                if(count==1 || count!=1 && j!=count-1){
                    for(int k=0; k<gap; k++){
                        b.append(' ');
                    }
                }
            }
            while(b.length()<maxWidth){
                b.append(' ');
            }
            result.add(b.toString());
        }
        return result;
    }
}
