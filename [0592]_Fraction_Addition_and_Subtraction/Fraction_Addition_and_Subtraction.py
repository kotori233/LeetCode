class Solution(object):

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        numerators, denominators, temp = [], [], ''
        expression += '+'
        for c in expression:
            if temp and c in '+-':
                a, b = temp.split('/')
                numerators.append(int(a))
                denominators.append(int(b))
                temp = ''
            temp += c
        de = 1
        for b in denominators:
            de *= b
        nu = sum([de / b * a for a, b in zip(numerators, denominators)])
        c = abs(gcd(nu, de))
        return '%d/%d' % (nu / c, de / c)
