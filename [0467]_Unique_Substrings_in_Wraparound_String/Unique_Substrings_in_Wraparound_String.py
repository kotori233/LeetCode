class Solution(object):

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        sheet = {}
        count = 0
        for i in range(len(p)):
            if i and (ord(p[i]) - ord(p[i - 1]) == 1 or
                      (p[i] == 'a' and p[i - 1] == 'z')):
                count += 1
            else:
                count = 1
            sheet[p[i]] = max(count, sheet.get(p[i], 0))
        return sum(sheet.values())
