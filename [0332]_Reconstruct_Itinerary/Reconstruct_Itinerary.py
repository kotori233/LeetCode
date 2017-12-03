class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.res = []

        def visited(pos):
            while sheet.get(pos, []):
                visited(sheet[pos].pop(0))
            self.res.append(pos)

        sheet = {}
        for each in sorted(tickets):
            sheet[each[0]] = sheet.get(each[0], []) + [each[1]]
        visited('JFK')
        return self.res[::-1]
