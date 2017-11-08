class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        subres = []
        i = 1
        while 1:
            length = len(subres)
            if length == k:
                res.append(subres[:])
                if subres[0] == n - k + 1:
                    return res
                i = subres.pop() + 1
            elif i > n - k + 1 + length:
                i = subres.pop() + 1
            else:
                subres.append(i)
                i += 1
