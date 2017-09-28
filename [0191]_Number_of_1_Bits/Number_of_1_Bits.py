class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans
