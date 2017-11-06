class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'
        res = ''
        f = 1
        for i in range(2, n):
            f *= i
        nums = [i for i in range(1, n + 1)]
        i = n - 1
        k -= 1
        while i:
            res += str(nums.pop(k // f))
            k %= f
            f //= i
            i -= 1
        return res + str(nums.pop(k // f))
