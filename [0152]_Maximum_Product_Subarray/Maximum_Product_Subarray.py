class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        max_l, min_l, max_g = 1, 1, nums[0]
        for i in nums:
            if i == 0:
                max_g = max(max_g, 0)
                max_l, min_l = 1, 1
            elif i < 0:
                temp = min_l * i
                max_g = max(max_g, temp)
                min_l = max_l * i
                max_l = max(1, temp)
            else:
                max_l *= i
                min_l *= i
                max_g = max(max_g, max_l)
        return max_g
