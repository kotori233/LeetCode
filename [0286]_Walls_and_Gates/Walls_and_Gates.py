class Solution(object):

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(i, j, val):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if rooms[i][j] >= val:
                rooms[i][j] = val
                dfs(i - 1, j, val + 1)
                dfs(i + 1, j, val + 1)
                dfs(i, j - 1, val + 1)
                dfs(i, j + 1, val + 1)

        n = len(rooms)
        m = len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
