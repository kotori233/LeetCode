class Solution(object):

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sheet = {}
        for index, value in enumerate(nums):
            sheet[value] = index
        for i in findNums:
            j = sheet[i] + 1
            try:
                while 1:
                    if nums[j] > i:
                        res.append(nums[j])
                        break
                    j += 1
            except IndexError:
                res.append(-1)
        return res
