class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, res = 0, 0
        try:
            while 1:
                res += nums[i]
                i += 2
        except IndexError:
            pass
        return res
