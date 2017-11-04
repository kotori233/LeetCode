class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1), len(num2)
        tmpres = [0] * (n1 + n2)
        res = ''
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(n1):
            for j in range(n2):
                tmpres[i + j] += int(num1[i]) * int(num2[j])
        for i in range(n1 + n2 - 1):
            tmpres[i + 1] += (tmpres[i] // 10)
            res = str(tmpres[i] % 10) + res
        if tmpres[-1] != 0:
            res = str(tmpres[-1]) + res
        return res
