class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = '123456789'
        space = [[] for i in range(9)]
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                if board[i][j] in d:
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False
                    n = i // 3 * 3 + j // 3
                    if board[i][j] not in space[n]:
                        space[n].append(board[i][j])
                    else:
                        return False
                if board[j][i] in d:
                    if board[j][i] not in column:
                        column.append(board[j][i])
                    else:
                        return False
        return True
