class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        sheet = {}
        for i in range(len(nums)):
            key = nums[i] // (t + 1)
            if key in sheet:
                return True
            if key + 1 in sheet and abs(nums[i] - sheet[key + 1]) <= t:
                return True
            if key - 1 in sheet and abs(nums[i] - sheet[key - 1]) <= t:
                return True
            sheet[key] = nums[i]
            if i >= k:
                del sheet[nums[i - k] // (t + 1)]
        return False
