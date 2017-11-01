class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step = 2 * numRows - 2
        res = s[::step]
        start = 1
        while start < numRows - 1:
            temp = ''
            j = step - 2 * start
            i = start
            while 1:
                try:
                    temp += s[i]
                    temp += s[i + j]
                except IndexError:
                    break
                i += step
            res += temp
            start += 1
        return res + s[numRows - 1::step]
