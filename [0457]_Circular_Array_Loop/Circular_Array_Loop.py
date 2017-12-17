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
            slow, fast = i, nextCur(i)
            while nums[slow] * nums[fast] > 0 and \
                    nums[slow] * nums[nextCur(fast)] > 0:
                if slow == fast:
                    if fast == nextCur(slow):
                        break
                    return True
                slow = nextCur(slow)
                fast = nextCur(nextCur(fast))
            slow = i
            val = nums[slow]
            while nums[slow] * val > 0:
                nums[slow] = 0
                slow = nextCur(slow)
        return False
