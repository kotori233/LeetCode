class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        sheet = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in sheet and i - sheet[x] <= k:
                return True
            else:
                sheet[x] = i
        return False
