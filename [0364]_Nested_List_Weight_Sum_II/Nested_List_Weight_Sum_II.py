class Solution(object):

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[List[int]]
        :rtype: int
        """
        res, pre = 0, 0
        while nestedList:
            nextList = []
            for i in nestedList:
                if isinstance(i, int):
                    pre += i
                else:
                    nextList.extend(i)
            res += pre
            nestedList = nextList
        return res
