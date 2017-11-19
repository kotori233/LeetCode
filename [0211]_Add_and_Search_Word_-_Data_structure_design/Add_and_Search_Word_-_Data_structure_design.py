class TireNode():

    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        father = self.root
        for i in word:
            child = father.children.get(i)
            if child is None:
                child = TireNode()
                father.children[i] = child
            father = child
        father.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(node, word):
            if word == '':
                if node.isWord:
                    return True
                return False
            if word[0] == '.':
                for each in node.children.values():
                    if dfs(each, word[1:]):
                        return True
            else:
                node = node.children.get(word[0])
                if node is None:
                    return False
                if dfs(node, word[1:]):
                    return True
            return False

        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
