class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        isbreak = [False for i in range(n + 1)]
        isbreak[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if isbreak[j] and s[j:i] in wordDict:
                    isbreak[i] = True
        return isbreak[n]
