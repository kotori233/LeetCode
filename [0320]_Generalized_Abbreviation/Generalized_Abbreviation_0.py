class Solution(object):

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        res = []
        for i in range(2 ** n):
            subres, d, count = '', i, 0
            for j in range(n):
                if d & 1 == 0:
                    temp = str(count) if count else ''
                    subres = word[-1 - j] + temp + subres
                    count = 0
                else:
                    count += 1
                d >>= 1
            if count:
                res.append(str(count) + subres)
            else:
                res.append(subres)
        return res
