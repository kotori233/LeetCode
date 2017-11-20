class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '+'
        stack = []
        d, flag = 0, '+'
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif s[i].isdigit():
                d = d * 10 + int(s[i])
            else:
                if flag == '+':
                    stack.append(d)
                    d = 0
                elif flag == '-':
                    stack.append(-d)
                    d = 0
                elif flag == '*':
                    stack.append(stack.pop() * d)
                    d = 0
                elif flag == '/':
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-((-temp) // d))
                    else:
                        stack.append(temp // d)
                    d = 0
                flag = s[i]
        return sum(stack)
