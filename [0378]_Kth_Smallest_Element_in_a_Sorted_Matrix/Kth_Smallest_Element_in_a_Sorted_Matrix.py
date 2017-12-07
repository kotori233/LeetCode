class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq

        n = len(matrix)
        queue = [(matrix[0][0], 0, 0)]
        for x in range(k):
            val, i, j = heapq.heappop(queue)
            if j == 0 and i + 1 < n:
                heapq.heappush(queue, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(queue, (matrix[i][j + 1], i, j + 1))
        return val
