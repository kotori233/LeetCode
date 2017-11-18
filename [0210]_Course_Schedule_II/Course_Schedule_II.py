class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        degree = [0 for i in range(numCourses)]
        sheet = {}
        for each in prerequisites:
            for i in each[1:]:
                degree[each[0]] += 1
                sheet[i] = sheet.get(i, []) + [each[0]]
        queue = []
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                res.append(i)
        while queue:
            try:
                for i in sheet[queue.pop(0)]:
                    degree[i] -= 1
                    if degree[i] == 0:
                        queue.append(i)
                        res.append(i)
            except KeyError:
                pass
        if sum(degree) != 0:
            return []
        return res
