class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.cache = {}

        def breakinput(input):
            if input.isdigit():
                return [int(input)]
            if input in self.cache:
                return self.cache[input]
            res = []
            for i in range(len(input)):
                if input[i] in '+-*':
                    left = breakinput(input[:i])
                    right = breakinput(input[i + 1:])
                    for p in left:
                        for q in right:
                            if input[i] == '+':
                                res.append(p + q)
                            elif input[i] == '-':
                                res.append(p - q)
                            elif input[i] == '*':
                                res.append(p * q)
            self.cache[input] = res
            return res

        return breakinput(input)
