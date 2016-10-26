# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        eof = False
        buffer = ['']*4
        ptr = 0
        while not eof:
            bytesread = min(read4(buffer), n-ptr)
            if bytesread<4:
                eof = True
            for i in range(ptr, ptr+bytesread):
                buf[i] = buffer[i-ptr]
            ptr += bytesread
        return ptr

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        boolean eof = false;
        char[] buffer = new char[4];
        int pos = 0;
        while(!eof && pos<n){
            int size = read4(buffer);
            if(size<4){
                eof = true;
            }
            int bytesread = Math.min(n-pos, size);
            System.arraycopy(buffer, 0, buf, pos, bytesread);
            pos += bytesread;
        }
        return pos;
    }
}
