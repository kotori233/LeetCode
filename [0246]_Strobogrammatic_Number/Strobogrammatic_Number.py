class Solution(object):

    def isStrobogrammatic(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sheet = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        num = str(num)
        if num in sheet:
            return True
        left, right = 0, len(num) - 1
        while left <= right:
            nl, nr = num[left], num[right]
            if nl not in sheet or nr not in sheet:
                return False
            if sheet[nl] != nr:
                return False
            left += 1
            right -= 1
        return True
