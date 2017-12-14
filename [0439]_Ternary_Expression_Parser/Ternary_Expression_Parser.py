class Solution(object):

    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for i in reversed(expression):
            if stack and stack[-1] == '?':
                # '?'
                stack.pop()
                t = stack.pop()
                # ':'
                stack.pop()
                f = stack.pop()
                if i == 'T':
                    stack.append(t)
                else:
                    stack.append(f)
            else:
                stack.append(i)
        return stack[-1]
