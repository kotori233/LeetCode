class Solution(object):

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def helper(i, j):
            count, temp = 0, []
            for d in dirs:
                x, y = i, j
                x += d[0]
                y += d[1]
                if -1 < x < n and -1 < y < m and board[x][y] == 'M':
                    count += 1
                else:
                    temp.append((x, y))
            if count:
                board[i][j] = str(count)
                return
            board[i][j] = 'B'
            for x, y in temp:
                if -1 < x < n and -1 < y < m and board[x][y] == 'E':
                    helper(x, y)

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        n = len(board)
        m = len(board[0])
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        elif board[i][j] == 'E':
            helper(i, j)
        return board
