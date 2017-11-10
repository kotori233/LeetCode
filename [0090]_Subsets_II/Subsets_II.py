class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            temp = subres if i and nums[i] == nums[i - 1] else res
            subres = []
            for each in temp:
                subres.append(each + [nums[i]])
            res += subres
        return res
