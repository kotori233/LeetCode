from collections import defaultdict


class Solution(object):

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        sheet = defaultdict(set)
        for father, child in zip(ppid, pid):
            sheet[father].add(child)
        queue = [kill]
        res = []
        while queue:
            father = queue.pop(0)
            res.append(father)
            for child in sheet[father]:
                queue.append(child)
        return res
