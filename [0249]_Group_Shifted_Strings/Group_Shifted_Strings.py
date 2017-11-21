class Solution(object):

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[str]
        """
        def update(s):
            shift = ord(s[0]) - 97
            if shift == 0:
                return s
            res = ''
            for i in s:
                temp = ord(i) - shift
                if temp < 97:
                    temp += 26
                res += chr(temp)
            return res

        sheet = {}
        for i in strings:
            temp = update(i)
            sheet[temp] = sheet.get(temp, []) + [i]
        res = []
        for i in sheet:
            temp = sheet[i]
            temp.sort(key=lambda x: x[0])
            res.append(temp)
        return res
