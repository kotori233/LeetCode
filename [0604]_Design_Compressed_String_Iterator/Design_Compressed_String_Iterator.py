class StringIterator(object):

    def __init__(self, compressedString):
        """
        Initialize your data structure here.
        """
        self.chars, self.nums = [], []
        self.count = 0
        self.cur = 0
        temp = ''
        for i in compressedString:
            if i.isdigit():
                temp += i
            else:
                try:
                    self.chars.append(i)
                    self.nums.append(int(temp))
                    temp = ''
                except ValueError:
                    pass
        self.nums.append(int(temp))

    def next(self):
        """
        if the original string still has uncompressed characters,
        return the next letter; Otherwise return a white space.
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.count == self.nums[self.cur]:
            self.cur += 1
            self.count = 1
        else:
            self.count += 1
        return self.chars[self.cur]

    def hasNext(self):
        """
        Judge whether there is any letter needs to be uncompressed.
        :rtype: bool
        """
        if self.cur == len(self.chars) - 1 and self.count == self.nums[-1]:
            return False
        return True
