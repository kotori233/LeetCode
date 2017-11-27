class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        d = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(n):
            for j in range(m):
                count = 0
                for k in range(8):
                    x = i + d[k][0]
                    y = j + d[k][1]
                    if -1 < x < n and -1 < y < m:
                        if board[x][y] in (1, 2):
                            count += 1
                if board[i][j] in (1, 2):
                    if count < 2 or count > 3:
                        board[i][j] = 2
                elif count == 3:
                    board[i][j] = 3
        for i in range(n):
            for j in range(m):
                board[i][j] %= 2
