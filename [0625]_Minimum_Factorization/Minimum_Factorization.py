class Solution(object):

    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1
        cnt = [0 for i in range(10)]
        for i in range(9, 1, -1):
            while not a % i:
                a /= i
                cnt[i] += 1
        if a > 1:
            return 0
        res = int(''.join(str(i) * cnt[i] for i in range(2, 10)))
        return min(res, 0x7FFFFFFF)
