class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        tofill = 1
        for node in preorder:
            tofill -= 1
            if tofill < 0:
                return False
            if node != '#':
                tofill += 2
        return not tofill
