class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.cur = 0

        def dfs():
            res = ''
            count = ''
            while self.cur < n:
                if s[self.cur].isdigit():
                    count += s[self.cur]
                    self.cur += 1
                elif s[self.cur] == '[':
                    self.cur += 1
                    sub = dfs()
                    res += (int(count) * sub)
                    count = ''
                elif s[self.cur] == ']':
                    self.cur += 1
                    return res
                else:
                    res += s[self.cur]
                    self.cur += 1
            return res

        n = len(s)
        return dfs()
