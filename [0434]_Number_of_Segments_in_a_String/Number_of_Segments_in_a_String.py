class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        count = 1
        for i in range(len(s) - 1):
            if s[i].isspace() and not s[i + 1].isspace():
                count += 1
        return count
