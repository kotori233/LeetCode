class Solution(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r, d, n = [], [], len(senate)
        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r0, d0 = r.pop(0), d.pop(0)
            if r0 > d0:
                d.append(d0 + n)
            else:
                r.append(r0 + n)
        return 'Radiant' if not d else 'Dire'
