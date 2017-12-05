class Solution(object):

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        if z == 0:
            return True
        if x + y >= z and z % gcd(x, y) == 0:
            return True
        return False
