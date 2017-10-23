class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        wide = int(sqrt(area))
        while 1:
            length = area // wide
            if length * wide == area:
                return (length, wide)
            wide -= 1
