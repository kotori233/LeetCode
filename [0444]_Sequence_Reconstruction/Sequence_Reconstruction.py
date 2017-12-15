from collections import defaultdict


class Solution(object):

    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        n = len(org)
        degree = [0 for i in range(n)]
        sheet = defaultdict(set)
        for each in seqs:
            if any(i < 1 or i > n for i in each):
                return False
            for i in range(1, len(each)):
                if each[i] not in sheet[each[i - 1]]:
                    sheet[each[i - 1]].add(each[i])
                    degree[each[i] - 1] += 1
        queue = [i for i in org if not degree[i - 1]]
        for i in range(n):
            if len(queue) != 1 or queue[0] != org[i]:
                return False
            dot = queue.pop()
            for j in sheet[dot]:
                degree[j - 1] -= 1
                if not degree[j - 1]:
                    queue.append(j)
        return True
