class Solution(object):

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # list subgames
        subgames = []
        count = 0
        s += '-'
        for i in range(len(s)):
            if s[i] == '+':
                count += 1
            if s[i] == '-':
                if count > 1:
                    subgames.append(count)
                count = 0
        # get sg-value
        sg = [0, 0]
        side = max(subgames) + 1
        for i in range(2, side):
            temp = set()
            for j in range(i // 2):
                temp.add(sg[j] ^ sg[i - j - 2])
            count = 0
            while count in temp:
                count += 1
            sg.append(count)
        # combine subgames
        res = 0
        for i in subgames:
            res ^= sg[i]
        return res > 0
