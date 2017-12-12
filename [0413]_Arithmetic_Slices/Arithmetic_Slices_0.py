class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count, res = 2, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
            else:
                if count > 2:
                    res += ((count - 1) * (count - 2) // 2)
                    count = 2
        if count > 2:
            res += ((count - 1) * (count - 2) // 2)
        return res
