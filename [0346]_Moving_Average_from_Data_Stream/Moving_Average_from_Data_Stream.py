class MovingAverage(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.queue = []
        self.length = n

    def next(self, val):
        """
        Calculate the moving average of all integers in the sliding window.
        :type val: int
        :rtype: float
        """
        length = len(self.queue)
        if length >= self.length:
            self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue) / min(3, length + 1)
