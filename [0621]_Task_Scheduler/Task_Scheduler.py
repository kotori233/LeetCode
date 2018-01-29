from collections import Counter


class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        t_max = max(count.values())
        t_sum = len(tasks)
        return t_sum + \
            max(0, (t_max - 1) * (n + 1) - sum(i - (i == t_max)
                                               for i in count.values()))
