class Solution(object):

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.visited = [False for i in range(10)]

        def dfs(num, count, res):
            if count >= m:
                res += 1
            count += 1
            if count > n:
                return res
            self.visited[num] = True
            for i in range(1, 10):
                temp = jump[num][i]
                if not self.visited[i] and (not temp or self.visited[temp]):
                    res = dfs(i, count, res)
            self.visited[num] = False
            return res

        jump = [[0 for i in range(10)] for j in range(10)]
        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5
        return dfs(1, 1, 0) * 4 + dfs(2, 1, 0) * 4 + dfs(5, 1, 0)
