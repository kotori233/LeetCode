class Solution(object):

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edgest: List[List[int]]
        :rtype: int
        """
        self.visited = [False for i in range(n)]

        def dfs(node):
            for i in sheet.get(node, []):
                if not self.visited[i]:
                    self.visited[i] = True
                    dfs(i)

        sheet = {}
        res = 0
        for each in edges:
            sheet[each[0]] = sheet.get(each[0], []) + [each[1]]
            sheet[each[1]] = sheet.get(each[1], []) + [each[0]]
        for i in range(n):
            if not self.visited[i]:
                res += 1
                dfs(i)
        return res
