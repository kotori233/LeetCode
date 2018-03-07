class Solution(object):

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def solve(polynomial):
            x_cnt, d_cnt = 0, 0
            flag, cnt = 1, ''
            polynomial += '+'
            for i in polynomial:
                if i == 'x':
                    x_cnt += int(cnt or '1') * flag
                    flag, cnt = 1, ''
                elif i in '+-':
                    d_cnt += int(cnt or '0') * flag
                    cnt = ''
                    flag = 1 if i == '+' else -1
                else:
                    cnt += i
            return x_cnt, d_cnt

        left, right = equation.split('=')
        lx, ld = solve(left)
        rx, rd = solve(right)
        x, d = lx - rx, rd - ld
        if x:
            return 'x=%d' % (d / x)
        elif d:
            return 'No solution'
        return 'Infinite solutions'
