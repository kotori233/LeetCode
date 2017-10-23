class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        temp, m = 0, 0
        for i in range(n):
            if nums[i] == 1:
                temp += 1
            if nums[i] == 0 and nums[i - 1] == 1:
                m = max(m, temp)
                temp = 0
        return max(m, temp)
