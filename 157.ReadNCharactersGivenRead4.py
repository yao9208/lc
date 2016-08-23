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
