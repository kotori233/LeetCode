class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        h = [0 for i in range(n + 1)]
        h[0] = h[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                h[i] += h[j] * h[i - 1 - j]
        return h[n]
