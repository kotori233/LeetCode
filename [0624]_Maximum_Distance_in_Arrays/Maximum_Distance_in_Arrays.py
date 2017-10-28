class Solution(object):

    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = 0
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        i = 1
        try:
            while 1:
                min_temp = arrays[i][0]
                max_temp = arrays[i][-1]
                res = max(res, abs(min_num - max_temp),
                          abs(max_num - min_temp))
                max_num = max(max_num, max_temp)
                min_num = min(min_num, min_temp)
                i += 1
        except IndexError:
            return res
