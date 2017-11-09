class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n
        count = 2
        flag = True if nums[0] == nums[1] else False
        for each in nums[2:]:
            if nums[count - 1] != each:
                count += 1
                nums[count - 1] = each
                flag = False
            elif not flag and nums[count - 1] == each:
                count += 1
                nums[count - 1] = each
                flag = True
        return count
