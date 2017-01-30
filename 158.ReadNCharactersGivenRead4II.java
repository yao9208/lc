/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    char[] buffer = new char[4];
    int offset = 0, len = 0;
    public int read(char[] buf, int n) {
        int ptr = 0;
        boolean eof = false;
        while(!eof && ptr<n){
            int size = len>0? len:read4(buffer);
            if(len==0 && size<4) eof = true;
            int needread = Math.min(size, n-ptr);
            System.arraycopy(buffer, offset, buf, ptr, needread);
            offset = (offset+needread)%4;
            len = size - needread;
            ptr += needread;
        }
        return ptr;
    }
}
