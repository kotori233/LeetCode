class Solution(object):

    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [1, 1 + k]
        for i in range(k - 1):
            if i % 2:
                res.append(res[-2] - 1)
            else:
                res.append(res[-2] + 1)
        return res + list(range(k + 2, n + 1))
