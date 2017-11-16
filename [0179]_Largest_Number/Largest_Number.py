class Solution:

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(lambda a, b: int(
            a + b) - int(b + a)), reverse=True)
        res = ''.join(nums).lstrip('0')
        if res == '':
            return '0'
        return res
