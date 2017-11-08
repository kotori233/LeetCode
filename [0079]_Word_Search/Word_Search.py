class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        self.searched = [[False for j in range(n)] for i in range(m)]

        def dfs(i, j, word):
            if word == '':
                return True
            if i and not self.searched[i - 1][j] and \
                    board[i - 1][j] == word[0]:
                self.searched[i - 1][j] = True
                if dfs(i - 1, j, word[1:]):
                    return True
                self.searched[i - 1][j] = False
            if j and not self.searched[i][j - 1] and \
                    board[i][j - 1] == word[0]:
                self.searched[i][j - 1] = True
                if dfs(i, j - 1, word[1:]):
                    return True
                self.searched[i][j - 1] = False
            if i < m - 1 and not self.searched[i + 1][j] and \
                    board[i + 1][j] == word[0]:
                self.searched[i + 1][j] = True
                if dfs(i + 1, j, word[1:]):
                    return True
                self.searched[i + 1][j] = False
            if j < n - 1 and not self.searched[i][j + 1] and \
                    board[i][j + 1] == word[0]:
                self.searched[i][j + 1] = True
                if dfs(i, j + 1, word[1:]):
                    return True
                self.searched[i][j + 1] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.searched[i][j] = True
                    if dfs(i, j, word[1:]):
                        return True
                    self.searched[i][j] = False
        return False
