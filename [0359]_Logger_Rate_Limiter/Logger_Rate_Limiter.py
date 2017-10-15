class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sheet = {}.fromkeys(range(1, 11))
        self.last = 0

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false. The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp < 11:
            if message not in self.sheet.values():
                self.sheet[timestamp] = message
                return True
            return False
        diff = timestamp - max(10, self.last)
        self.last = timestamp
        for i in range(1, 10):
            try:
                self.sheet[i] = self.sheet[i + diff]
            except KeyError:
                self.sheet[i] = None
        self.sheet[10] = None
        if message not in self.sheet.values():
            self.sheet[10] = message
            return True
        return False
