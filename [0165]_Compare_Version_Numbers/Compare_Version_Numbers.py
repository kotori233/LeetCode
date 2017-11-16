class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ret1 = version1.split('.')
        ret2 = version2.split('.')
        i = 0
        flag1, flag2 = True, True
        while flag1 or flag2:
            try:
                a = int(ret1[i])
            except IndexError:
                flag1 = False
                a = 0
            try:
                b = int(ret2[i])
            except IndexError:
                flag2 = False
                b = 0
            if a > b:
                return 1
            if b > a:
                return -1
            i += 1
        return 0
