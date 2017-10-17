class Solution(object):

    def validWordAbbreviation(self, s, abbr):
        """
        :type s: str
        :type abbr: str
        :rtype: bool
        """
        s += 'x'
        abbr += 'x'
        i = j = 0
        while i < len(abbr):
            tab = '0'
            while abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                tab += abbr[i]
                i += 1
            j += int(tab)
            try:
                if abbr[i] != s[j]:
                    return False
            except IndexError:
                return False
            i += 1
            j += 1
        try:
            s[j]
            return False
        except IndexError:
            return True
