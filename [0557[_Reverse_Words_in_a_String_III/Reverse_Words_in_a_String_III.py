class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = s[::-1].split(' ')
        res = ''
        for i in ret:
            res = ' ' + i + res
        return res[1:]
