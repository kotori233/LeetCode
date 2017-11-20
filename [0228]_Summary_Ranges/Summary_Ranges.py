class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if nums == []:
            return res
        left = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                right = nums[i - 1]
                if left == right:
                    res.append(str(left))
                else:
                    res.append('%d->%d' % (left, right))
                left = nums[i]
        right = nums[-1]
        if left == right:
            res.append(str(left))
        else:
            res.append('%d->%d' % (left, right))
        return res
