class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stack = []
        for node in preorder:
            while stack and stack[-1] == '#' and node == '#':
                stack.pop()
                try:
                    stack.pop()
                except IndexError:
                    return False
            stack.append(node)
        return stack == ['#']
