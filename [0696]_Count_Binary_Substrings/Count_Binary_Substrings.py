class Solution(object):

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_s, pre_n, temp, res = None, None, 0, 0
        for i in s:
            if pre_s is None:
                pre_s = i
                temp += 1
            elif i == pre_s:
                temp += 1
            elif pre_n is None:
                pre_n = temp
                pre_s = i
                temp = 1
            else:
                res += min(temp, pre_n)
                pre_n = temp
                pre_s = i
                temp = 1
        if pre_n:
            return res + min(temp, pre_n)
        return res
