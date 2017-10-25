class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i, n = 0, len(s)
        res = ''
        while i < n:
            if i == 0:
                res += s[k - 1::-1]
            else:
                res += s[i + k - 1:i - 1:-1]
            res += s[i + k:i + k + k]
            i += 2 * k
        return res
