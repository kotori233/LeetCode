class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import random
        while 1:
            r = random.choice(nums)
            if nums.count(r) > len(nums) // 2:
                return r
