class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            board[i][j] = '#'
            if i and board[i - 1][j] == 'O':
                dfs(i - 1, j)
            if j and board[i][j - 1] == 'O':
                dfs(i, j - 1)
            if i < n - 1 and board[i + 1][j] == 'O':
                dfs(i + 1, j)
            if j < m - 1 and board[i][j + 1] == 'O':
                dfs(i, j + 1)

        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        if m == 0:
            return
        for i in range(n):
            if board[i][0] != 'X':
                dfs(i, 0)
            if board[i][m - 1] != 'X':
                dfs(i, m - 1)
        for j in range(m):
            if board[0][j] != 'X':
                dfs(0, j)
            if board[n - 1][j] != 'X':
                dfs(n - 1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
