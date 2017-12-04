class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag, self.rdiag, self.n = 0, 0, n

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        d = 1 if player == 1 else -1
        self.rows[row] += d
        self.cols[col] += d
        if row == col:
            self.diag += d
        if row + col == self.n - 1:
            self.rdiag += d
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or \
                abs(self.diag) == self.n or abs(self.rdiag) == self.n:
            return player
        return 0
