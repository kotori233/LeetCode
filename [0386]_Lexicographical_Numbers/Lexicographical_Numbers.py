class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.res = []

        def dfs(k):
            if k > n:
                return
            self.res.append(k)
            k *= 10
            if k > n:
                return
            for i in range(10):
                dfs(k + i)

        for i in range(1, 10):
            dfs(i)
        return self.res
