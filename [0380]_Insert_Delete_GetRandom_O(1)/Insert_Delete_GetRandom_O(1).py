class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sheet = {}
        self.nums = []
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
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.sheet:
            return False
        remove_idx = self.sheet[val]
        swap_val = self.nums.pop()
        if self.idx != remove_idx:
            self.sheet[swap_val] = remove_idx
            self.nums[remove_idx] = swap_val
        del self.sheet[val]
        self.idx -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random

        idx = random.choice(range(self.idx + 1))
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom(){\rtf1}
