class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        for i in tokens:
            if i == '+':
                res.append(res.pop() + res.pop())
            elif i == '-':
                temp = res.pop()
                res.append(res.pop() - temp)
            elif i == '*':
                res.append(res.pop() * res.pop())
            # Python 3 写法
            # elif i == '/':
            #     temp = res.pop()
            #     res.append(int(res.pop() / temp))
            #
            # Python 2/3 通用写法
            elif i == '/':
                a = res.pop()
                b = res.pop()
                if (a < 0) ^ (b < 0):
                    res.append(-((-b) // a))
                else:
                    res.append(b // a)
            else:
                res.append(int(i))
        return res[0]
