class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict0 = {}
        # enumerate() 返回可迭代对象的索引和值
        for index, value in enumerate(nums):
            x = target - value
            if x in dict0.keys():
                return [index, dict0[x]]
            else:
                dict0[value] = index
        return []
