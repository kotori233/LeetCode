class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect

        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            pos = sum([bisect.bisect_right(each, mid) for each in matrix])
            if k <= pos:
                right = mid - 1
            else:
                left = mid + 1
        return left
