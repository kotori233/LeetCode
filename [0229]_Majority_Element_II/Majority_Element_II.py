class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return nums
        base = n // 3
        res = []
        nums.sort()
        left = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                right = i
                if right - left > base:
                    res.append(nums[left])
                left = i
        right = n
        if right - left > base:
            res.append(nums[left])
        return res
