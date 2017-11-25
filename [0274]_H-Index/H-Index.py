class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n):
            if i and citations[i] == citations[i - 1]:
                continue
            h = max(h, min(n - i, citations[i]))
        return h
