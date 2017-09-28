class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            # 取最后一位
            ans |= n & 1
            ans <<= 1
            n >>= 1
        return ans >> 1
