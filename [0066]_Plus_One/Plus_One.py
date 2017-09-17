class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = ''
        for i in digits:
            nums += str(i)
        nums = str(int(nums) + 1)
        ans = []
        for i in nums:
            ans.append(int(i))
        return ans
