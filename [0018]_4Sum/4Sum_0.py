class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n = set(), len(nums)
        if n < 4:
            return []
        sheet = {}
        nums.sort()
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = nums[i] + nums[j]
                if temp in sheet:
                    sheet[temp].append((i, j))
                else:
                    sheet[temp] = [(i, j)]
        for i in sheet:
            temp = target - i
            if temp in sheet:
                for k in sheet[i]:
                    for j in sheet[temp]:
                        if k[0] < k[1] < j[0] < j[1]:
                            res.add((nums[k[0]], nums[k[1]],
                                     nums[j[0]], nums[j[1]]))
        return [list(i) for i in res]
