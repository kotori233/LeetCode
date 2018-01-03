class Solution(object):

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p1, p2 = a.find('+'), b.find('+')
        x1, y1 = int(a[:p1]), int(a[p1 + 1:-1])
        x2, y2 = int(b[:p2]), int(b[p2 + 1:-1])
        x, y = x1 * x2 - y1 * y2, x1 * y2 + x2 * y1
        return '%d+%di' % (x, y)
