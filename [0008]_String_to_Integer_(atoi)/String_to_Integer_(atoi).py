class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        negative, temp = False, ''
        if not str[0].isdigit():
            if str[0] == '-':
                negative = True
            elif str[0] != '+':
                return 0
        else:
            temp += str[0]
        i = 1
        while 1:
            try:
                if not str[i].isdigit():
                    if temp == '':
                        return 0
                    break
                else:
                    temp += str[i]
            except IndexError:
                if str[i - 1] in ('+', '-'):
                    return 0
                break
            i += 1
        if negative:
            return max(-int(temp), -2147483648)
        return min(int(temp), 2147483647)
