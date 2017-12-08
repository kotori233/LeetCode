class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sheet = {}
        self.idx = -1

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sheet:
            return False
        self.idx += 1
        self.sheet[val] = self.idx
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.sheet:
            return False
        del self.sheet[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random

        return random.choice(self.sheet.keys())


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
