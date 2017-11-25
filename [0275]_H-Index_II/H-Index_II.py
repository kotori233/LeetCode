class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if n - middle == citations[middle]:
                return n - middle
            if n - middle > citations[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return n - left
