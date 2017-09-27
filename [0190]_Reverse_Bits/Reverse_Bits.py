class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        n = bin(n)[-1:1:-1]
        length = len(n)
        n += '0' * (32 - length)
        return int(n, 2)
