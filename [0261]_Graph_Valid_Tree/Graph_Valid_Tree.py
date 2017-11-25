class Solution(object):

    def validTree(self, n, edges):
        """
        :type edges: List[List[int]]
        :type n: int
        :rtype: bool
        """
        degree = [0 for i in range(n)]
        sheet = {}
        for each in edges:
            degree[each[1]] += 1
            degree[each[0]] += 1
            sheet[each[0]] = sheet.get(each[0], []) + [each[1]]
            sheet[each[1]] = sheet.get(each[1], []) + [each[0]]
        if 0 in degree:
            return False
        queue = []
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        while queue:
            for i in sheet[queue.pop(0)]:
                degree[i] -= 1
                if degree[i] == 1:
                    queue.append(i)
        return sum(degree) == 0
