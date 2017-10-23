class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def isonerow(word, key):
            for i in word:
                if i not in key:
                    return False
            return True

        keys = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        res = []
        for each in words:
            for i in range(3):
                if each[0] in keys[i] and isonerow(each, keys[i]):
                    res.append(each)
        return res
