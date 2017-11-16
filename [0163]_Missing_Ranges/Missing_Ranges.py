class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        # 空数组时
        if n == 0:
            if upper - lower > 0:
                res.append('%d->%d' % (lower, upper))
            else:
                res.append(str(lower))
            return res
        # lower与nums[0]之间
        if nums[0] - lower > 1:
            res.append('%d->%d' % (lower, nums[0] - 1))
        elif nums[0] - lower == 1:
            res.append(str(lower))
        if n == 1:
            return res
        # 数组之间
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 2:
                res.append('%d->%d' % (nums[i - 1] + 1, nums[i] - 1))
            elif nums[i] - nums[i - 1] == 2:
                res.append(str(nums[i] - 1))
        # nums[n - 1]与upper之间
        if upper - nums[n - 1] > 1:
            res.append('%d->%d' % (nums[n - 1] + 1, upper))
        elif upper - nums[n - 1] == 1:
            res.append(str(upper - 1))
        return res
