class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[int]
        :rtype: int
        """
        res = 0
        father = nestedList
        count = 1
        while 1:
            child = []
            for i in father:
                if isinstance(i, int):
                    res += (i * count)
                else:
                    child.extend(i)
            if child == []:
                break
            father = child
            count += 1
        return res
