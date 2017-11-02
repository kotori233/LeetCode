class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []

        def create(s, left, right):
            if not (left or right):
                self.res.append(s)
            if left:
                create(s + '(', left - 1, right)
            if left < right:
                create(s + ')', left, right - 1)

        if n:
            create('', n, n)
        return self.res
