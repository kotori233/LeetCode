class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def myPow(a, b):
            if b == 0 or a == 1:
                return 1
            if b == 1:
                return a
            k = b // 2
            return myPow(a, k) * myPow(a, b - k) % 1337

        a %= 1337
        res = 1
        for i in range(len(b)):
            res = myPow(res, 10) * myPow(a, b[i]) % 1337
        return res
