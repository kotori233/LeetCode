class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sheet = {}
        for i in nums:
            sheet[i] = sheet.get(i, 0) + 1
        res = []
        for i, v in sorted(sheet.items(), reverse=True, key=lambda x: x[1]):
            res.append(i)
            if len(res) == k:
                return res
