class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack, count = [], k
        for i in num:
            while stack and count and i < stack[-1]:
                stack.pop()
                count -= 1
            stack.append(i)
        res = ''.join(stack[:len(num) - k]).lstrip('0')
        return res if res else '0'
