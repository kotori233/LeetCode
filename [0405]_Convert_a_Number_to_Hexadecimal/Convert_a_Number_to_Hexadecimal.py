class Solution(object):

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        sheet = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = ''
        if num < 0:
            num &= 0xFFFFFFFF
        while num != 0:
            temp = num & 0xF
            if temp < 10:
                res = str(temp) + res
            else:
                res = sheet[temp] + res
            num >>= 4
        return res
