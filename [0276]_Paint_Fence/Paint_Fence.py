class Solution(object):

    def numWays(self, n, k):
        """
        :type nums: List[int]
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        ret = [0] * (n + 1)
        ret[1], ret[2] = k, k * k
        for i in range(3, n + 1):
            # 3与2颜色不同，共(k - 1) * ret[i - 1]
            # 3与2颜色相同（与1不同），共(k - 1) * ret[i - 2]
            ret[i] = (k - 1) * (ret[i - 1] + ret[i - 2])
        return ret[n]
