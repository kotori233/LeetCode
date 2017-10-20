class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        i = 0
        while i < n:
            sheet = {}
            j = 0
            while j < n:
                if i != j:
                    d = (points[i][0] - points[j][0]) ** 2 + \
                        (points[i][1] - points[j][1]) ** 2
                    sheet[d] = sheet.get(d, 0) + 1
                j += 1
            for k in sheet.values():
                if k > 1:
                    res += k * (k - 1)
            i += 1
        return res
