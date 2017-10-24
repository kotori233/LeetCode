class Solution(object):

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = ''
        flag = True
        if num < 0:
            num = -num
            flag = False
        while num:
            res = str(num % 7) + res
            num //= 7
        if flag:
            return res
        return '-' + res
