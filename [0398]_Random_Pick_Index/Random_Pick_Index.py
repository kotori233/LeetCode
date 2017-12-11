import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, count = -1, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randint(1, count) == 1:
                    res = i
        return res
