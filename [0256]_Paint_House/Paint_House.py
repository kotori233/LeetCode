class Solution(object):

    def minCost(self, costs):
        """
        :type costs: List[List]
        :rtype: int
        """
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        m = min(costs[i][0], costs[i][1], costs[i][2])
        return m
