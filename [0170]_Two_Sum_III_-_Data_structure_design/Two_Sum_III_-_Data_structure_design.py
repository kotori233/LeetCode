class TwoSum:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = {}

    def add(self, number):
        """
        :type number: int
        :rtype: void
        """
        self.stack.get(number, 0) + 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        x = value / 2
        if x in self.stack and self.stack[x] > 1:
            return True
        for i in self.stack:
            if value - i in self.stack:
                return True
        return False
