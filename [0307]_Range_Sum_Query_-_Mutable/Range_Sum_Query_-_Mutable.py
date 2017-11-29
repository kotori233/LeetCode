class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # import math

        def buildTree(start, end, root):
            if start == end:
                self.tree[root] = nums[start]
                return self.tree[root]
            middle = (start + end) // 2
            temp1 = buildTree(start, middle, root * 2 + 1)
            temp2 = buildTree(middle + 1, end, root * 2 + 2)
            self.tree[root] = temp1 + temp2
            return self.tree[root]

        if nums != []:
            self.nums = nums
            n = len(nums)
            # 线段树空间 2 * (2 ** int(math.ceil(math.log(len(nums), 2)))) - 1
            self.tree = [0 for i in range(4 * n)]
            buildTree(0, n - 1, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def updateTree(start, end, root):
            if i > end or i < start:
                return
            self.tree[root] += diff
            if start == end:
                return
            middle = (start + end) // 2
            updateTree(start, middle, root * 2 + 1)
            updateTree(middle + 1, end, root * 2 + 2)

        diff = val - self.nums[i]
        self.nums[i] = val
        updateTree(0, len(self.nums) - 1, 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumTree(start, end, root):
            if i <= start and j >= end:
                return self.tree[root]
            if i > end or j < start:
                return 0
            middle = (start + end) // 2
            return sumTree(start, middle, root * 2 + 1) + \
                sumTree(middle + 1, end, root * 2 + 2)

        if i == j:
            return self.nums[i]
        return sumTree(0, len(self.nums) - 1, 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
