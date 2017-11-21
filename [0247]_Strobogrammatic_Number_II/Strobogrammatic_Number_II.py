class Solution(object):

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = ['']
        i = n % 2
        if i == 1:
            res = ['0', '1', '8']
        while i <= n - 2:
            temp = []
            print('a')
            for each in res:
                if i != n - 2:
                    temp.append('0' + each + '0')
                temp.append('1' + each + '1')
                temp.append('6' + each + '9')
                temp.append('8' + each + '8')
                temp.append('9' + each + '6')
            res = temp
            i += 2
        return res
