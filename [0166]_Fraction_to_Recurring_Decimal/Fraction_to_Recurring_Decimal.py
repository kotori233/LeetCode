class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return
        if numerator == 0:
            return '0'
        res = '-' if (numerator < 0) ^ (denominator < 0) else ''
        a, b = abs(numerator), abs(denominator)
        res += str(a // b)
        remainder = a % b
        if remainder == 0:
            return res
        res += '.'
        sheet, temp, i = {}, '', 0
        while remainder:
            if remainder in sheet:
                start, end = sheet[remainder], i
                if start > 0:
                    res += temp[:start]
                return res + '(' + temp[start:end] + ')'
            else:
                sheet[remainder] = i
            remainder *= 10
            temp += str(remainder // b)
            remainder %= b
            i += 1
        return res + temp
