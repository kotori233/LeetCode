class Solution(object):

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edgest: List[List[int]]
        :rtype: int
        """
        val = list(range(n))
        res = n
        for each in edges:
            if val[each[0]] != val[each[1]]:
                res -= 1
                val[each[1]] = val[each[0]]
        return res
