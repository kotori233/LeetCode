class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        nums = [1 for i in range(k)]
        curs = [0 for i in range(k)]
        res = [1]
        pre = 1
        for i in range(n - 1):
            for j in range(k):
                if nums[j] == pre:
                    nums[j] = res[curs[j]] * primes[j]
                    curs[j] += 1
            pre = min(nums)
            res.append(pre)
        return res[-1]
