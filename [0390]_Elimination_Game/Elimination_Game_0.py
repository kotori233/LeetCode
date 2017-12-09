class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def update(n, flag):
            if n == 1:
                return 1
            if flag:
                # 删奇数
                return 2 * update(n // 2, False)
            elif n % 2:
                # 映射为2n
                return 2 * update(n // 2, True)
            else:
                # 映射为2n-1
                return 2 * update(n // 2, True) - 1

        return update(n, True)
