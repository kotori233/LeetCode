from collections import defaultdict


class Solution(object):

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        sheet = defaultdict(list)
        for each in paths:
            each = each.split(' ')
            for f in each[1:]:
                i = f.rfind('(')
                sheet[f[i:]].append(each[0] + '/' + f[:i])
        return [sheet[p] for p in sheet if len(sheet[p]) != 1]
