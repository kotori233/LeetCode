class Solution(object):

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        n = len(board)
        if n == 0:
            return res
        m = len(board[0])
        if m == 0:
            return res
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.' or (i and board[i - 1][j] == 'X') or \
                        (j and board[i][j - 1] == 'X'):
                    continue
                res += 1
        return res
