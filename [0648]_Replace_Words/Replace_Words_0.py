class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        father = self.root
        for c in word:
            child = father.children.get(c)
            if child is None:
                child = TrieNode()
                father.children[c] = child
            father = child
        father.isWord = True

    def search(self, word):
        node = self.root
        res = ''
        for c in word:
            node = node.children.get(c)
            if node is None:
                break
            res += c
            if node.isWord:
                return res
        return word


class Solution(object):

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)
        ans = []
        for word in sentence.split():
            ans.append(trie.search(word))
        return ' '.join(ans)
