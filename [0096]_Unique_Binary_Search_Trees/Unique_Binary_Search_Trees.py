class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        fat1 = 1
        for i in range(n + 2, n * 2 + 1):
            fat1 *= i
        fat2 = 1
        for i in range(1, n + 1):
            fat2 *= i
        return fat1 // fat2
