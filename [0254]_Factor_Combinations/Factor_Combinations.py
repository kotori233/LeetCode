class Solution(object):

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(n, subres, start):
            end = int(n ** 0.5) + 1
            if len(subres) > 0:
                self.res.append(subres + [n])
            if end < start:
                return
            for i in range(start, end):
                if n % i == 0:
                    dfs(n // i, subres + [i], i)

        dfs(n, [], 2)
        return self.res
