class Solution(object):

    def isReflected(self, points):
        """
        :type m: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        sheet = defaultdict(set)
        max_x, min_x = float('-inf'), float('inf')
        for each in points:
            max_x = max(max_x, each[0])
            min_x = min(min_x, each[0])
            sheet[each[1]].add(each[0])
        middle = max_x + min_x
        for each in points:
            if middle - each[0] not in sheet[each[1]]:
                return False
        return True
