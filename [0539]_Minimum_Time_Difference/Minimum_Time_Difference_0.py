class Solution(object):

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time = [False for i in range(1440)]
        res, left, right, pre = float('inf'), float('inf'), float('-inf'), 0
        for t in timePoints:
            idx = 60 * int(t[:2]) + int(t[-2:])
            if time[idx]:
                return 0
            time[idx] = True
        for i in range(1440):
            if time[i]:
                if left != float('inf'):
                    res = min(res, i - pre)
                left = min(left, i)
                right = max(right, i)
                pre = i
        return min(res, 1440 + left - right)
