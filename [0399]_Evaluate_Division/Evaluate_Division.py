from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        sheet = defaultdict(lambda: defaultdict(int))
        for (s1, s2), val in zip(equations, values):
            sheet[s1][s2] = val
            sheet[s2][s1] = 1.0 / val
        for i in sheet:
            sheet[i][i] = 1.0
            for s1 in sheet:
                for s2 in sheet:
                    if sheet[s1][i] and sheet[i][s2]:
                        sheet[s1][s2] = sheet[s1][i] * sheet[i][s2]
        return [sheet[s1][s2] if sheet[s1][s2] else -1.0 for s1, s2 in queries]
