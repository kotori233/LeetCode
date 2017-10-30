class Solution(object):

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, b = len(A), len(B)
        if a < b:
            times = b // a
            if B in A * times:
                return times
            if B in A * (times + 1):
                return times + 1
        else:
            if B in A:
                return 1
            if B in A * 2:
                return 2
        return -1
