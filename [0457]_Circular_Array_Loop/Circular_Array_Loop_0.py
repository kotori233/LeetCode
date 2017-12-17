class Solution(object):

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def nextCur(x):
            return (x + nums[x] + n) % n

        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            cur, count = i, 0
            while count < n:
                count += 1
                temp = nextCur(cur)
                if cur == temp or nums[cur] * nums[temp] < 0:
                    break
                cur = temp
            if count == n:
                return True
            cur = i
            while count:
                nums[cur] = 0
                cur = nextCur(cur)
                count -= 1
        return False
