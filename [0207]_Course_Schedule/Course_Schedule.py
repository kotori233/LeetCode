class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        sheet = {}
        degree = [0 for i in range(numCourses)]
        for each in prerequisites:
            for i in each[-1:0:-1]:
                degree[each[0]] += 1
                sheet[i] = sheet.get(i, []) + [each[0]]
        queue = []
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            try:
                for i in sheet[queue.pop(0)]:
                    degree[i] -= 1
                    if degree[i] == 0:
                        queue.append(i)
            except KeyError:
                pass
        return sum(degree) == 0
