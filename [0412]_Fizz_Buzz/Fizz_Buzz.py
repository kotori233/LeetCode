class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [''] * n
        i = 1
        while i < n + 1:
            if i % 3 == 0:
                res[i - 1] += 'Fizz'
            if i % 5 == 0:
                res[i - 1] += 'Buzz'
            if res[i - 1] == '':
                res[i - 1] += str(i)
            i += 1
        return res
