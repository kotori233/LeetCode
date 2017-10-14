class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        ret = [0] * n
        if n != 0:
            ret[0] = nums[0]
            for i in range(1, n):
                ret[i] = ret[i - 1] + nums[i]
        self.allsum = ret

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.allsum[j]
        return self.allsum[j] - self.allsum[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
