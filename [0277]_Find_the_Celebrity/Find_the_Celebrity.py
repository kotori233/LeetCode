class Solution(object):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n):
            if know(res, i):
                res = i
        for i in range(n):
            if res != i and (know(res, i) or not know(i, res)):
                return -1
        return res
