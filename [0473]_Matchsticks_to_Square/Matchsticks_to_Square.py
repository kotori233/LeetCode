class Solution(object):

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(idx, filled):
            if idx == n:
                return True
            for i in range(4):
                if filled[i] >= nums[idx]:
                    filled[i] -= nums[idx]
                    if dfs(idx + 1, filled):
                        return True
                    filled[i] += nums[idx]
            return False

        n = len(nums)
        if n == 0 or n < 4:
            return False
        girth = sum(nums)
        if girth % 4:
            return False
        nums.sort(reverse=True)
        side = girth // 4
        filled = [side for i in range(4)]
        return dfs(0, filled)
