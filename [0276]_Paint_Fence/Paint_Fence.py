class Solution(object):

    def numWays(self, n, k):
        """
        :type nums: List[int]
        :type n: int
        :type k: int
        :rtype: int
        """
        ret = [0] * n
        ret[1], ret[2] = k, k * k
        if n < 3:
            return ret[n]
        for i in range(3, n + 1):
            # 3与2颜色不同，共(k - 1) * ret[i - 1]
            # 3与2颜色相同（与1不同），共(k - 1) * ret[i - 2]
            ret[i] = (k - 1) * (ret[i - 1] + ret[i - 2])
        return ret[n]
