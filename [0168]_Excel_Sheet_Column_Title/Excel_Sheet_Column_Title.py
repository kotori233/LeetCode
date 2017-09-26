class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while 1:
            x = (n - 1) % 26
            ans = chr(x + 65) + ans
            n = (n - 1) // 26
            if n == 0:
                break
        return ans
