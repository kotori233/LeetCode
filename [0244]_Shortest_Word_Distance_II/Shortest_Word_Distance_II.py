class WordDistance(object):

    def __init__(self, words):
        """
        Initialize your data structure here.
        :type words: List[str]
        """
        self.sheet = {}
        for index, value in enumerate(words):
            self.sheet[value] = self.sheet.get(value, []) + [index]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = 0x7FFFFFFF
        list1 = self.sheet[word1]
        list2 = self.sheet[word2]
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            m = min(m, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return m


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
