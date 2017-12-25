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

        d.sort(key=lambda x: (-len(x), x))
        for t in d:
            if isSubsequence(t, s):
                return t
        return ''
