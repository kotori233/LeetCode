class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        sheet, res, stack = {}, [], ['JFK']
        for each in sorted(tickets):
            sheet[each[0]] = sheet.get(each[0], []) + [each[1]]
        while stack:
            while sheet.get(stack[-1], []):
                stack.append(sheet[stack[-1]].pop(0))
            res.append(stack.pop())
        return res[::-1]
