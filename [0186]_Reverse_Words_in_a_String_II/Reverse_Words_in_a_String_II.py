class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(' ')
        if s == '':
            return s
        temp = ''
        res = ''
        for i in range(len(s)):
            if s[i] != ' ':
                temp = s[i] + temp
            elif i and s[i] == ' ' and s[i - 1] == ' ':
                pass
            else:
                res += temp
                res += ' '
                temp = ''
        res += temp
        return res[::-1]
