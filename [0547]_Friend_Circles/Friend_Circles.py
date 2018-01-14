class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for j in range(n):
                if M[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)

        n = len(M)
        visited = [False for i in range(n)]
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count
