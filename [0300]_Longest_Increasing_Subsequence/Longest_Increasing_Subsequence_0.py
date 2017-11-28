class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for each in nums:
            left, right = 0, len(dp)
            while left < right:
                middle = (left + right) // 2
                if dp[middle] < each:
                    left = middle + 1
                else:
                    right = middle
            try:
                dp[right] = each
            except IndexError:
                dp.append(each)
        return len(dp)
