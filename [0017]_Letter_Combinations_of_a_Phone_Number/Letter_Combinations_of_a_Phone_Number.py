class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.sheet = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                      '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        def combine(d, res):
            new_res = []
            for i in self.sheet[d]:
                new_res += [each + i for each in res]
            return new_res

        if digits == '':
            return []
        res = ['']
        for i in digits:
            res = combine(i, res)
        return res
