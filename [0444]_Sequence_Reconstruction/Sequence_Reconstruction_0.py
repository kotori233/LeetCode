class Solution(object):

    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        sheet = {v: i for i, v in enumerate(org)}
        edges = set()
        for each in seqs:
            if any(i not in sheet for i in each):
                return False
            for i in range(1, len(each)):
                if sheet[each[i]] < sheet[each[i - 1]]:
                    return False
                edges.add((each[i - 1], each[i]))
        for i in range(1, len(org)):
            if (org[i - 1], org[i]) not in edges:
                return False
        return True
