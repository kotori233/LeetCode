class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        ready = []
        i = 1
        while i * i <= n:
            ready.append(i * i)
            i += 1
        father = {n}
        res = 0
        while father:
            res += 1
            child = set()
            for i in father:
                for j in ready:
                    if i - j == 0:
                        return res
                    if i - j > 0:
                        child.add(i - j)
                    else:
                        break
            father = child
