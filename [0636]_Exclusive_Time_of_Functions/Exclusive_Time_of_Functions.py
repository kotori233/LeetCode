class Solution(object):

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0 for i in range(n)]
        stack = []
        for each in logs:
            idx, state, t = each.split(':')
            idx, t = int(idx), int(t)
            if state == 'start':
                if stack:
                    sidx, st = stack[-1]
                    res[sidx] += (t - st)
                stack.append([idx, t])
            else:
                sidx, st = stack[-1]
                res[sidx] += (t - st + 1)
                stack.pop()
                if stack:
                    stack[-1][1] = t + 1
        return res
