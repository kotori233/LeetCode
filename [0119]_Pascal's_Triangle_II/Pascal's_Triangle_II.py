class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = [1, 1]
        n = 1
        while n < rowIndex:
            row.append(1)
            for i in range(len(row) - 2, 0, -1):
                row[i] = row[i] + row[i - 1]
            n += 1
        return row
