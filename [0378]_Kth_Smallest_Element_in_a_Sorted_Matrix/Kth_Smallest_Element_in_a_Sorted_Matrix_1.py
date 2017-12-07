class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def lower_count(m):
            res = 0
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= m:
                    j += 1
                    res += (i + 1)
                else:
                    i -= 1
            return res

        left, right = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        while left <= right:
            mid = (left + right) // 2
            pos = lower_count(mid)
            if k <= pos:
                right = mid - 1
            else:
                left = mid + 1
        return left
