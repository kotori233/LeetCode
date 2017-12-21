class Solution(object):

    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        nums = list(range(1, n + 2))
        res, i = [], 0
        while i < n:
            if s[i] == 'I':
                res += [nums.pop(0)]
                i += 1
            else:
                count = 1
                while i < n and s[i] == 'D':
                    count += 1
                    i += 1
                res += nums[:count][::-1]
                nums = nums[count:]
        return res + nums
