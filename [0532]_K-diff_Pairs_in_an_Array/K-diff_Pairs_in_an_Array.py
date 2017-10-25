class Solution(object):

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < 2 or k < 0:
            return 0
        res = 0
        if k == 0:
            sheet = {}
            for i in nums:
                sheet[i] = sheet.get(i, 0) + 1
            for i in sheet:
                if sheet[i] > 1:
                    res += 1
            return res
        nums = set(nums)
        for i in nums:
            if i + k in nums:
                res += 1
        return res
