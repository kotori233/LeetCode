class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        ns = '#' + '#'.join(s) + '#'
        n, p, middle, i, m = len(ns), [0, 1], 1, 2, 0
        while i < n:
            flag = False
            temp2 = middle + p[middle] - i
            # i不在middle管辖范围内(case1)
            if temp2 < 0:
                p.append(0)
                flag = True
            else:
                temp1 = 2 * middle - i
                # i在middle管辖范围内，且i管辖范围在middle范围内(case2)
                if p[temp1] < temp2:
                    p.append(p[temp1])
                # i在middle管辖范围内，但i管辖范围一部分超出middle范围(case3)
                else:
                    p.append(temp2)
                    flag = True
            # 对超出部分进行验证(case1,case3)
            if flag:
                j = p[i] + 1
                while 1:
                    if i - j > -1 and i + j < n and ns[i - j] == ns[i + j]:
                        p[i] += 1
                    else:
                        break
                    j += 1
            # 转移政治中心middle
            if p[i] > p[middle]:
                middle = i
            # 维护最大值
            if m < p[i]:
                m = p[i]
                mi = i
            i += 1
            # 后面的没戏了
            if m > n - 2 - i:
                break
        return s[(mi - m + 1) // 2:(mi + m + 1) // 2]
