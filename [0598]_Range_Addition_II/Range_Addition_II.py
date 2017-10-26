class Solution(object):

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m * n
        max_a = min([ops[i][0] for i in range(len(ops))])
        max_b = min([ops[i][1] for i in range(len(ops))])
        return max_a * max_b
