class Solution(object):

    def splitLoopedString(self, strs):
        """
        :type strs: str
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]
        res = ''
        for idx, s in enumerate(strs):
            for cut in (s, s[::-1]):
                for i in range(len(s) + 1):
                    res = max(res, cut[i:] +
                              ''.join(strs[idx + 1:] + strs[:idx]) + cut[:i])
        return res
