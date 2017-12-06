class Solution(object):

    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0 for i in range(length)]
        for each in updates:
            res[each[0]] += each[2]
            try:
                res[each[1] + 1] -= each[2]
            except IndexError:
                pass
        for i in range(1, length):
            res[i] += res[i - 1]
        return res
