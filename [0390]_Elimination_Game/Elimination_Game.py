class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        # 强行偶数模式（前后成对去除）
        return 2 * (1 + n // 2 - self.lastRemaining(n // 2))
