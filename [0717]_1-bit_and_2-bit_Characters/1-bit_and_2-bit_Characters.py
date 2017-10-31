class Solution(object):

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, count = -2, 0
        while 1:
            try:
                if bits[i] == 1:
                    count += 1
                    i -= 1
                else:
                    break
            except IndexError:
                break
        return count % 2 == 0
