from collections import defaultdict


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dis(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        sheet = defaultdict(int)
        points = (p1, p2, p3, p4)
        for i in range(4):
            for j in range(i + 1, 4):
                sheet[dis(points[i], points[j])] += 1
        return 4 in sheet.values() and 2 in sheet.values()
