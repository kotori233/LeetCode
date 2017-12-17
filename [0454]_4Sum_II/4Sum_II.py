from collections import defaultdict


class Solution(object):

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sheet1, sheet2 = defaultdict(int), defaultdict(int)
        n = len(A)
        for i in range(n):
            for j in range(n):
                sheet1[A[i] + B[j]] += 1
                sheet2[C[i] + D[j]] += 1
        res = 0
        for i in sheet1:
            if -i in sheet2:
                res += sheet1[i] * sheet2[-i]
        return res
