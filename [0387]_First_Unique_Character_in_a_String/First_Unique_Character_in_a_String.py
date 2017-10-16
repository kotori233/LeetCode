class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sheet = {}
        res = n = len(s)
        for i in range(n):
            if s[i] in sheet:
                sheet[s[i]].append(i)
            else:
                sheet[s[i]] = [i]
        for i in sheet.values():
            try:
                i[1]
            except IndexError:
                res = min(res, i[0])
        if res == n:
            return -1
        return res
