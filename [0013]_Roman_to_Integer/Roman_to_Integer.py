class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        dict0 = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s)):
            x += dict0[s[i]]
            if dict0[s[i]] > dict0[s[i - 1]] and i > 0:
                x -= 2 * dict0[s[i - 1]]
        return x
