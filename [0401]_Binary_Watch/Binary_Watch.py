class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        # bin(763) = '0b1011111011'
        for i in range(764):
            if bin(i).count('1') == num:
                h = i >> 6
                m = i & 0x3F
                if h < 12 and m < 60:
                    res.append('%d:%02d' % (h, m))
        return res
