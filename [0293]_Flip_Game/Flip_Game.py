class Solution(object):

    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 2:
            return []
        res = []
        temp = s[0]
        for i in range(1, n):
            if s[i] == '+' and temp == '+':
                new_s = s[:i - 1] + '--' + s[i + 1:]
                res.append(new_s)
            temp = s[i]
        return res
