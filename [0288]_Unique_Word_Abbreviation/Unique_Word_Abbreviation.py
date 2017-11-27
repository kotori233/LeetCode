class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        Initialize your data structure here.
        :type dictionary: List[str]
        """
        self.sheet = {}
        for each in dictionary:
            n = len(each) - 2
            if n > 0:
                abbr = each[0] + str(n) + each[-1]
            else:
                abbr = each
            if abbr not in self.sheet:
                self.sheet[abbr] = {each}
            else:
                self.sheet[abbr].add(each)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word) - 2
        if n > 0:
            abbr = word[0] + str(n) + word[-1]
        else:
            abbr = word
        if abbr not in self.sheet:
            return True
        return self.sheet[abbr] == {word}
