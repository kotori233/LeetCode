class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        ret = [1] * n
        end = int(n ** 0.5 + 1)
        for i in range(2, end):
            if ret[i]:
                j = i + i
                while j < n:
                    ret[j] = 0
                    j += i
        return sum(ret) - 2
