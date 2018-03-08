class Solution(object):

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(reverse=True)
        cur = [float('inf'), float('inf')]
        res = 0
        for p in pairs:
            if p[1] < cur[0]:
                res += 1
                cur = p
        return res
