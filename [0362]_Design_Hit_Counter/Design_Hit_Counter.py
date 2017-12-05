class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [0 for i in range(300)]
        self.hits = [0 for i in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        :type timestamp: int
        :rtype: void
        """
        idx = timestamp % 300
        if self.time[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.time[idx] = timestamp
            self.hits[idx] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                res += self.hits[i]
        return res
