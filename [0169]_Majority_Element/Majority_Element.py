class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict0 = {}
        n = len(nums) // 2
        for i in nums:
            dict0[i] = dict0.get(i, 0) + 1
            if dict0[i] > n:
                return i
