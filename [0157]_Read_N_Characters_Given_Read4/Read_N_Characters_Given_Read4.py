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
        numBytes = 0
        while n > 0:
            # 新建缓冲区
            buf4 = [None] * 4
            # 读入缓冲区，并返回大小
            size = read4(buf4)
            minLen = min(size, n - numBytes)
            if minLen == 0:
                break
            for i in range(minLen):
                buf[numBytes] = buf4[i]
                numBytes += 1
        return numBytes
