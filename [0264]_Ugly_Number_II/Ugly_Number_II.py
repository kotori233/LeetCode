class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        t1, t2, t3 = 0, 0, 0
        while len(res) < n:
            n1, n2, n3 = 2 * res[t1], 3 * res[t2], 5 * res[t3]
            res.append(min(n1, n2, n3))
            if res[-1] == n1:
                t1 += 1
            if res[-1] == n2:
                t2 += 1
            if res[-1] == n3:
                t3 += 1
        return res[-1]
