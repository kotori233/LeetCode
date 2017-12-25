class Solution(object):

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sheet = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            t = total % k if k else total
            if t in sheet:
                if i - sheet[t] > 1:
                    return True
            else:
                sheet[t] = i
        return False
