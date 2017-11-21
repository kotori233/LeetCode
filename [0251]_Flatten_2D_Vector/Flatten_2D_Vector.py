class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here
        :type vec2d: List[List[int]]
        :rtype: int
        """
        self.row = 0
        self.col = 0
        self.vec2d = vec2d

    def next(self):
        """
        :rtype: int
        """
        self.col += 1
        return self.vec2d[self.row][self.col - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec2d) and \
                self.col == len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
