class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            (s, count) = queue.pop(0)
            if s == endWord:
                return count
            for i in range(len(s)):
                left = s[:i]
                right = s[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != s[i]:
                        new = left + j + right
                        if new in wordList:
                            queue.append((new, count + 1))
                            wordList.remove(new)
        return 0
