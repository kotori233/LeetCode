class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        tri = [[1], [1, 1]]
        k = 1
        while 1:
            pre_row = tri[k]
            next_row = [1]
            for i in range(1, len(pre_row)):
                next_row.append(pre_row[i - 1] + pre_row[i])
            next_row.append(1)
            tri.append(next_row)
            if k == numRows - 2:
                break
            k += 1
        return tri
