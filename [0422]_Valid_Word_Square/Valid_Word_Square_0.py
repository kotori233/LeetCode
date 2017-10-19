class Solution(object):

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        rows = len(words)
        if rows != len(words[0]):
            return False
        i = j = 0
        for i in range(rows):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except IndexError:
                    return False
        return True
