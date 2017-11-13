class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        sheet = {}
        visited = set()
        for each in wordList:
            for i in range(n):
                s = each[:i] + '#' + each[i + 1:]
                sheet[s] = sheet.get(s, []) + [each]
        queue = [(beginWord, 1)]
        while queue:
            (s, count) = queue.pop(0)
            if s not in visited:
                visited.add(s)
                if s == endWord:
                    return count
                for i in range(n):
                    new = s[:i] + '#' + s[i + 1:]
                    list0 = sheet.get(new, [])
                    for new in list0:
                        if new not in visited:
                            queue.append((new, count + 1))
        return 0
