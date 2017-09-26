class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.major(nums, 0, len(nums) - 1)

    def major(self, origin_nums, left, right):
        if left == right:
            return origin_nums[left]
        mid = (left + right) // 2
        major_l = self.major(origin_nums, left, mid)
        major_r = self.major(origin_nums, mid + 1, right)
        if major_l == major_r:
            return major_l
        count_l = origin_nums[left: right + 1].count(major_l)
        count_r = origin_nums[left: right + 1].count(major_r)
        if count_l > count_r:
            return major_l
        else:
            return major_r
