class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = 'aeiouAEIOU'
        ls = list(s)
        pos = []
        for i in range(len(ls)):
            if ls[i] in ret:
                pos.append(i)
        n = len(pos)
        if n < 2:
            return s
        for i in range(n // 2):
            ls[pos[i]], ls[pos[n - i - 1]] = ls[pos[n - i - 1]], ls[pos[i]]
        return ''.join(ls)
