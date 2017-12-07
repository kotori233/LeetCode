class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        p, q = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                p = q + 1
            elif nums[i] < nums[i - 1]:
                q = p + 1
        return max(p, q)
