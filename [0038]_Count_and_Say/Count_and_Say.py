class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        def count(seq):
            num = seq[0]
            statistics = 0
            new_seq = ''
            for i in range(0, len(seq)):
                if seq[i] == num:
                    statistics += 1
                else:
                    new_seq += str(statistics) + str(num)
                    num = seq[i]
                    statistics = 1
            if statistics != 0:
                new_seq += str(statistics) + str(num)
            return new_seq

        seq = '1'
        for i in range(1, n):
            seq = count(seq)
        return seq
