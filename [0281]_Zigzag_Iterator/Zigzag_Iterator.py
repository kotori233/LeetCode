class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.s1 = v1
        self.s2 = v2
        self.p1 = 0
        self.p2 = 0

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return
        if self.p1 > self.p2:
            temp = self.s2[self.p2]
            self.p2 += 1
        else:
            temp = self.s1[self.p1]
            self.p1 += 1
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p1 >= len(self.s1):
            self.p1 = 0x7FFFFFFF
        if self.p2 >= len(self.s2):
            self.p2 = 0x7FFFFFFF
        return not (self.p1 == 0x7FFFFFFF and self.p2 == 0x7FFFFFFF)
