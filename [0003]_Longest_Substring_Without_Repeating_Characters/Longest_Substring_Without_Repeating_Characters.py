class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        ret = []
        for i in s:
            if i in ret:
                m = max(m, len(ret))
                while ret.pop(0) != i:
                    pass
            ret.append(i)
        return max(m, len(ret))
