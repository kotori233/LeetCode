class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums
        self.c = [0 for i in range(self.n + 1)]
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += self.nums[i]
                k += (k & (-k))

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & (-i))

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        j += 1
        while j:
            res += self.c[j]
            j -= (j & (-j))
        while i:
            res -= self.c[i]
            i -= (i & (-i))
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
