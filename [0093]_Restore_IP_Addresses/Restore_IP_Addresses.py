class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []

        def dfs(count, s, subres):
            if count == 4:
                if s == '':
                    self.res.append(subres[:-1])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) < 256:
                        dfs(count + 1, s[i:], subres + s[:i] + '.')
                    if s[0] == '0':
                        break

        dfs(0, s, '')
        return self.res
