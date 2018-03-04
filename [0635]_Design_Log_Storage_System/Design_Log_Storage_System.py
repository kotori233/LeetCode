from collections import defaultdict


class LogSystem(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.gras = {'Year': 4, 'Month': 7, 'Day': 10,
                     'Hour': 13, 'Minute': 16, 'Second': 19}
        self.sheet = defaultdict(set)

    def put(self, id, timestamp):
        """
        Given a log's unique id and timestamp,
        store the log in your storage system.
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.sheet[timestamp].add(id)

    def retrieve(self, s, e, gra):
        """
        Return the id of logs whose timestamps are
        within the range from start to end.
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = set()
        degree = self.gras[gra]
        s, e = s[0:degree], e[0:degree]
        for t in self.sheet:
            if s <= t[0:degree] <= e:
                res.update(self.sheet[t])
        return list(res)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
