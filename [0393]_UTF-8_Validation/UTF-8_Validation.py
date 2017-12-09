class Solution(object):

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        k = 0
        for i in data:
            if i < 128:
                continue
            if i < 192:
                k -= 1
                if k < 0:
                    return False
            elif k or i > 247:
                return False
            elif i < 224:
                k = 1
            elif i < 240:
                k = 2
            else:
                k = 3
        return k == 0
