class Solution(object):

    def verifyPreorder(self, preorder):
        """
        :type n: List[int]
        :rtype: bool
        """
        min_val = 0x80000000
        stack = []
        for i in preorder:
            if i < min_val:
                return False
            while stack and stack[-1] < i:
                min_val = stack.pop()
            stack.append(i)
        return True
