class Solution(object):

    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        n = len(s)
        end = 0
        bold = [False for i in range(n)]
        for i in range(n):
            for each in dict:
                if s[i:].startswith(each):
                    end = max(end, i + len(each))
            bold[i] = end > i
        res = '<b>' if bold[0] else ''
        for i in range(n):
            if i and not bold[i] and bold[i - 1]:
                res += ('</b>' + s[i])
            elif i and bold[i] and not bold[i - 1]:
                res += '<b>' + s[i]
            else:
                res += s[i]
        if bold[-1]:
            res += '</b>'
        return res
