class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        length = len(pattern)
        if length != len(str):
            return False
        if length < 2:
            return True
        sheet = {}
        for i in range(length):
            temp = pattern[i]
            if temp in sheet:
                if sheet[temp] != str[i]:
                    return False
            else:
                if str[i] in sheet.values():
                    return False
                sheet[temp] = str[i]
        return True
