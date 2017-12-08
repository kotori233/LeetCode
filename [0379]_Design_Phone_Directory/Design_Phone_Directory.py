class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here.
        :type maxNumbers: int
        """
        self.used = [False for i in range(maxNumbers)]
        self.recycle = []
        self.next_num = 0
        self.maxNumbers = maxNumbers

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.recycle and self.next_num == self.maxNumbers:
            return -1
        if self.recycle:
            temp = self.recycle.pop()
        else:
            temp = self.next_num
            self.next_num += 1
        self.used[temp] = True
        return temp

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if 0 <= number < self.maxNumbers and not self.used[number]:
            return True
        return False

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if 0 <= number < self.maxNumbers and self.used[number]:
            self.used[number] = False
            self.recycle.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
