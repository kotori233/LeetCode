class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res, depth, n = 0, 0, len(input)
        input += '\n'
        sheet = {0: 0}
        i = 0
        while i < n:
            start = i
            while input[i] != '\n' and input[i] != '\t':
                i += 1
            if input[i] == '\n':
                if '.' in input[start: i]:
                    res = max(res, sheet[depth] + i - start)
                else:
                    depth += 1
                    sheet[depth] = sheet[depth - 1] + i - start + 1
                depth = 0
            else:
                depth += 1
            i += 1
        return res
