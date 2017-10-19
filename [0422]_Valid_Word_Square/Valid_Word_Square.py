class Solution(object):

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        rows = len(words)
        if rows != len(words[0]):
            return False
        i = 0
        while i < rows:
            try:
                column = ''
                for each in words:
                    column += each[i]
            except IndexError:
                pass
            if column != words[i]:
                return False
            i += 1
        return True
