class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        max_cur, min_cur, max_all, min_all = 0, 0, 0, 0
        sum_all, start_cur, end, start_all = 0, 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            sum_all += diff
            if max_cur < 0:
                max_cur = diff
                start_cur = i
            else:
                max_cur += diff
            if max_cur > max_all:
                max_all = max_cur
                start_all = start_cur
            if min_cur > 0:
                min_cur = diff
            else:
                min_cur += diff
            if min_cur < min_all:
                min_all = min_cur
                end = i
        if sum_all < 0:
            return -1
        if sum_all - min_all > max_all:
            return end + 1
        return start_all
