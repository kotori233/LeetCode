class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        step, left = 1, 1
        while left + step <= n:
            left += step
            step *= 2
            if left + step > n:
                break
            if n // step % 2:
                left += step
            step *= 2
        return left
