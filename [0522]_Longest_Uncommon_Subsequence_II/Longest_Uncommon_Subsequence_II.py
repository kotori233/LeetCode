class Solution(object):

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # if s1 is a subsequence of s2
        def isSubsequence(s1, s2):
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return i == len(s1)

        strs.sort(key=len, reverse=True)
        for i, s1 in enumerate(strs):
            if all(not isSubsequence(s1, s2)
                   for j, s2 in enumerate(strs) if i != j):
                return len(s1)
        return -1
