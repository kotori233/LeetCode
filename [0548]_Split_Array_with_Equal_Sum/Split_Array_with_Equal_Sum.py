class Solution(object):

    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 7:
            return False
        for i in range(1, n):
            nums[i] = nums[i - 1] + nums[i]
        for j in range(3, n - 3):
            sheet = set()
            for i in range(1, j - 1):
                if nums[i - 1] == nums[j - 1] - nums[i]:
                    sheet.add(nums[i - 1])
            for k in range(j + 1, n - 1):
                temp = nums[k - 1] - nums[j]
                if temp in sheet and temp == nums[n - 1] - nums[k]:
                    return True
        return False
