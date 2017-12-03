class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        if num == 0:
            return res
        for i in range(1, num + 1):
            res.append(res[i & (i - 1)] + 1)
        return res
