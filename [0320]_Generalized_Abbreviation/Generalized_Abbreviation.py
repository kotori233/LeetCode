class Solution(object):

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.res = []

        def dfs(cur, subres, digit):
            if cur == n:
                if digit:
                    subres += str(digit)
                self.res.append(subres)
                return
            temp = str(digit) if digit else ''
            dfs(cur + 1, subres + temp + word[cur], 0)
            dfs(cur + 1, subres, digit + 1)

        n = len(word)
        dfs(0, '', 0)
        return self.res
