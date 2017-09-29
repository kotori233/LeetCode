class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ret = []
        n = str(n)
        while 1:
            temp = 0
            for i in n:
                temp += int(i) ** 2
            if temp == 1:
                return True
            n = str(temp)
            if n in ret:
                return False
            ret.append(n)
