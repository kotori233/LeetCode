class Solution(object):

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        queue = [(start, 0)]
        while queue:
            gene, count = queue.pop(0)
            if gene == end:
                return count
            for i in range(8):
                left = gene[:i]
                right = gene[i + 1:]
                for j in 'ACGT':
                    if gene[i] != j:
                        new = left + j + right
                        if new in bank:
                            queue.append((new, count + 1))
                            bank.remove(new)
        return -1
