class Solution(object):

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n < 2:
            return True
        if word.islower():
            return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
        return False
