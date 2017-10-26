class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent, late = 0, 0
        for i in s:
            if i == 'A':
                absent += 1
            if i == 'L':
                late += 1
            else:
                late = 0
            if absent > 1 or late > 2:
                return False
        return True
