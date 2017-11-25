class Solution(object):

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []

        def dfs(sheet, subres):
            if len(subres) == n:
                self.res.append(subres)
                return
            for i in sheet:
                if sheet[i] > 1:
                    sheet[i] -= 2
                    dfs(sheet, i + subres + i)
                    sheet[i] += 2

        sheet = {}
        n = len(s)
        for i in s:
            sheet[i] = sheet.get(i, 0) + 1
        count, middle = 0, ''
        for i in sheet:
            if sheet[i] % 2 == 1:
                count += 1
                if count > 1:
                    return self.res
                middle = i
        dfs(sheet, middle)
        return self.res
