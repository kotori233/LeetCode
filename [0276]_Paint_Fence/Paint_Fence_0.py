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
        same, diff = k, k * (k - 1)
        for i in range(2, n + 1):
            res = same + diff
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff
        return res
