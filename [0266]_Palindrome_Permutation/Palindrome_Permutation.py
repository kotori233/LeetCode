class Solution(object):

    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = []
        for i in s:
            if i in ret:
                ret.remove(i)
            else:
                ret.append(i)
        return len(ret) == 1 or len(ret) == 0
