public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder b = new StringBuilder();
        for(String str:strs){
            int size = str.length();
            b.append(size).append('/').append(str);
        }
        return b.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i=0;
        while(i<s.length()){
            int slash = s.indexOf('/',i);
            int size = Integer.parseInt(s.substring(i, slash));
            String str = s.substring(slash+1, slash+1+size);
            result.add(str);
            i = slash+1+size;
        }
        return result;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
