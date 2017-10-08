class Solution(object):

    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = pos2 = None
        d = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            if words[i] == word2:
                pos2 = i
            try:
                d = min(d, abs(pos1 - pos2))
            except TypeError:
                pass
        return d
