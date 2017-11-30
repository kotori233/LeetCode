class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        queue = []
        res = [1]
        k = len(primes)
        for i in range(k):
            heapq.heappush(queue, (primes[i], 0, primes[i]))
        for i in range(n - 1):
            ans, cur, p = queue[0]
            res.append(ans)
            while queue[0][0] == ans:
                ans, cur, p = heapq.heappop(queue)
                heapq.heappush(queue, (p * res[cur + 1], cur + 1, p))
        return res[-1]
