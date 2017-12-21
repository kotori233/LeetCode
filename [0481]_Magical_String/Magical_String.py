class Solution(object):

    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = '122'
        cur = 2
        while len(s) < n:
            s += int(s[cur]) * str(3 - int(s[-1]))
            cur += 1
        return s[:n].count('1')
