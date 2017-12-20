class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            zero, one = 0, 0
            for each in nums:
                if each & (1 << i):
                    one += 1
                else:
                    zero += 1
            res += one * zero
        return res
