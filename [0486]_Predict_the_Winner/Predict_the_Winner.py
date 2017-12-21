class Solution(object):

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.cache = {}

        def helper(left, right):
            if left == right:
                return nums[left]
            if (left, right) not in self.cache:
                self.cache[(left, right)] = max(
                    nums[left] - helper(left + 1, right),
                    nums[right] - helper(left, right - 1))
            return self.cache[(left, right)]

        return helper(0, len(nums) - 1) >= 0
