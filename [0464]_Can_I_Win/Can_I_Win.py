class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.sheet = {}

        def helper(used, target):
            if used in self.sheet:
                return self.sheet[used]
            for i in range(maxChoosableInteger):
                mask = 1 << i
                if used & mask:
                    continue
                if i + 1 >= target or not helper(used | mask, target - i - 1):
                    self.sheet[used] = True
                    return True
            self.sheet[used] = False
            return False

        if maxChoosableInteger >= desiredTotal:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) < desiredTotal * 2:
            return False
        return helper(0, desiredTotal)
