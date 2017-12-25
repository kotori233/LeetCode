class Solution(object):

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubsequence(s1, s2):
            i = 0
            for j in s2:
                if i < len(s1) and s1[i] == j:
                    i += 1
            return i == len(s1)

        res = ''
        for t in d:
            if isSubsequence(t, s):
                if len(t) > len(res):
                    res = t
                elif len(t) == len(res) and t[0] < res[0]:
                    res = t
        return res
