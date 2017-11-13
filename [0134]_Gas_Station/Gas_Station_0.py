class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_all, sum_cur, start = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            sum_all += diff
            sum_cur += diff
            if sum_cur < 0:
                start = i + 1
                sum_cur = 0
        if sum_all < 0:
            return -1
        return start
