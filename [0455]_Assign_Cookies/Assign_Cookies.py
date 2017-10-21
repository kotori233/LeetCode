class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        while i < len(s):
            try:
                if s[i] >= g[j]:
                    res += 1
                    j += 1
            except IndexError:
                break
            i += 1
        return res
