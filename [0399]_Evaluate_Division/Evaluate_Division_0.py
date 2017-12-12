from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(s1, s2, visited):
            if s1 not in sheet or s2 not in sheet:
                return -1.0
            if s2 in sheet[s1]:
                return sheet[s1][s2]
            for each in sheet[s1]:
                if each not in visited:
                    val = dfs(each, s2, visited + [each])
                    if val != -1.0:
                        return sheet[s1][each] * val
            return -1.0

        sheet = defaultdict(dict)
        for (s1, s2), val in zip(equations, values):
            sheet[s1][s2] = val
            sheet[s2][s1] = 1.0 / val
        for i in sheet:
            sheet[i][i] = 1.0
        return [dfs(s1, s2, []) for s1, s2 in queries]
