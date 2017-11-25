class Codec(object):

    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        :type s: List[str]
        :rtype: str
        """
        res = ''
        for i in strs:
            res += (str(len(i)) + '#' + i)
        return res

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        res = []
        start = 0
        i = start
        while 1:
            try:
                if s[i] == '#':
                    length = int(s[start: i])
                    start = i + length + 1
                    res.append(s[i + 1: start])
                    i = start
                else:
                    i += 1
            except IndexError:
                return res
