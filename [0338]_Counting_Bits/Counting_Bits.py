class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0, 1]
        i, k = 1, 1
        while i < num:
            for i in range(2 ** k, 2 ** (k + 1)):
                if i > num:
                    break
                step = 2 ** k - 2 ** (k - 1)
                if i < 2 ** k + step:
                    res.append(res[i - step])
                else:
                    res.append(res[i - step] + 1)
            k += 1
        return res
